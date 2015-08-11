import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtSerialPort import *


class Reagent(object):
    def __init__(self, reagent_id):
        self.id_barcode=reagent_id
        self.transactionString=''
        self.reagentDataList=[]
        self.reagentdb=QSqlDatabase.addDatabase("QMYSQL",'self.reagentdb')
        self.reagentdb.setHostName("localhost")
        self.reagentdb.setDatabaseName("reagentsandhardware")
        self.reagentdb.setUserName("term_biotechlab")
        self.reagentdb.setPassword("terminalbiotechlabnqz89a93")
        okreagentdb=self.reagentdb.open()
        if not okreagentdb:
            print ('Could not open reagent DB')
            sys.exit(2)
        querystring='SELECT lot_number, reagent_name, reagent_group, amount, expiration_date, storage_location FROM reagents WHERE id_barcode="'+reagent_id+'"'
        print (querystring)
        retrivequery=QSqlQuery(querystring, self.reagentdb)
        if retrivequery.size()!=1:
            print ('Barcode is not uniqe')
        retrivequery.next()
        for i in range(6):
            self.reagentDataList.append(retrivequery.value(i))
        if len(self.reagentDataList)!=6:
            print ("Data was retrived but reading data into list from database was failed")
        print (self.reagentDataList)
        retrivequery.finish()
        self.residual_reagent_amount=self.reagentDataList[3]

    def get_reagent_name(self):
        return self.reagentDataList[1]

    def get_reagent_group(self):
        return self.reagentDataList[2]

    def get_exp_date(self):
        return self.reagentDataList[4]

    def get_amount(self):
        return self.reagentDataList[3]

    def get_storage_place(self):
        #//TODO implement access to storage location database and retriving storage place names and generating storage place label string
        return self.reagentDataList[5]

    def modify_amount(self, weighted_amount):
        self.residual_reagent_amount=str(float(self.reagentDataList[3])-float(weighted_amount))

    def set_transaction_info(self, operatorCode, weighted_amount, canceled=''):
        transactionDateTime=QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm:ss")
        print (transactionDateTime)
        self.transactionString=' NEW '+operatorCode+' '+str(transactionDateTime)+' '+weighted_amount+canceled

    def write_info_into_database(self,iscancelled):
        if iscancelled:
            transationLogingQueryString='UPDATE reagents SET transaction_log=CONCAT(transaction_log, "'+self.transactionString+'") WHERE id_barcode="'+self.id_barcode+'"'
            print (transationLogingQueryString)
            transationLogingQuery=QSqlQuery(transationLogingQueryString, self.reagentdb)
            transationLogingQuery.finish()
        else:
            modifyQueryString='UPDATE reagents SET amount="'+self.residual_reagent_amount+'" WHERE id_barcode="'+self.id_barcode+'"'
            modifyamountQuery=QSqlQuery(modifyQueryString, self.reagentdb)
            modifyamountQuery.finish()
            transationLogingQueryString='UPDATE reagents SET transaction_log=CONCAT(transaction_log, "'+self.transactionString+'") WHERE id_barcode="'+self.id_barcode+'"'
            print (transationLogingQueryString)
            transationLogingQuery=QSqlQuery(transationLogingQueryString, self.reagentdb)
            transationLogingQuery.finish()
            self.reagentdb.close()



class Operator(object):

    def __init__(self, operator_id):
        self.operator_id=operator_id
        self.operator_full_name=''
        #Create and open database connection
        self.userdb=QSqlDatabase.addDatabase("QMYSQL",'userdb')
        self.userdb.setHostName("localhost")
        self.userdb.setDatabaseName("users")
        self.userdb.setUserName("term_biotechlab")
        self.userdb.setPassword("terminalbiotechlabnqz89a93")
        okuserdb=self.userdb.open()
        if not okuserdb:
            print ('Could not open user DB')
            sys.exit(3)
        querystring='SELECT full_name FROM users_id WHERE rfid_id="'+operator_id+'"'
        retrivequery=QSqlQuery(querystring, self.userdb)
        if retrivequery.size()!=1:
            print ('RFID ID is not uniqe')
        retrivequery.next()
        self.operator_full_name=retrivequery.value(0)
        retrivequery.clear()
        self.userdb.close()
        self.userdb.removeDatabase('userdb')

    def get_operator_full_name(self):
        return self.operator_full_name

class Scales(object):

    def __init__(self,manufacturer):
        self.weighing=None
        self.availableSerialPorts=QSerialPortInfo.availablePorts()
        for port in self.availableSerialPorts:
            if port.manufacturer()==manufacturer:
                self.scaleCOM=QSerialPort(port)
        self.scaleCOM.setBaudRate(9600)
        self.notred=True

    def readWeightFromScale(self):
        newstring=None
        isopened=self.scaleCOM.open(QIODevice.ReadWrite)
        if not isopened:
            print ("Error opening COM-port", self.scaleCOM.error())
        if self.scaleCOM.waitForReadyRead(50):
            weight=self.scaleCOM.readAll()
            while  self.scaleCOM.waitForReadyRead(10):
                weight+=self.scaleCOM.readAll()
            strweight=QTextCodec.codecForMib(106).toUnicode(weight)
            newstring=strweight.strip('\r\n g')
            print (newstring)
            self.notred=False
        self.scaleCOM.close()
        if newstring is not None:
            self.weighing=str(float(newstring)*1000)
            return self.weighing
        else:
            return None

    def get_last_weight(self):
        return self.weighing



