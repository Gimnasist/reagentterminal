import sys
sys.path.append('interface')
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtSerialPort import *
from interface.RFIDScanDlg import *
from interface.scanBarcodeDlg import *
from interface.weightReagentDlg import *
from interface.confirmDlg import *
from interface.finishedDlg import *
from interface.reweightingReasonDlg import *

app=QApplication(sys.argv)
style=QStyleFactory.create('fusion')
app.setStyle(style)

#Creating all modelless dialogs for system
rfiddialog=RFIDScanDlg()
barcodedialog=scanBarcodeDlg()
weightingdialog=weightReagentDlg()
confirmdialog=confirmDlg()
finishdialog=finishedDlg()
reweightingreasondialog=reweightingReasonDlg()

#Functions to write changes to database
def write_changes_to_database(confirmdialogpointer):
    barcodedialog.current_reagent.modify_amount(weightingdialog.optainedWeighting)
    barcodedialog.current_reagent.set_transaction_info(rfiddialog.operator_rfid_code, weightingdialog.optainedWeighting, '')
    barcodedialog.current_reagent.write_info_into_database(False)

def write_info_about_reweighting(reason):
    barcodedialog.current_reagent.set_transaction_info(rfiddialog.operator_rfid_code, weightingdialog.optainedWeighting, ' '+reason)
    barcodedialog.current_reagent.write_info_into_database(True)


#Create all signal-slot connection
rfiddialog.rfidCodeObtained.connect(barcodedialog.prepareUIscanBarcodeDlg)
barcodedialog.reagentDataOptained.connect(weightingdialog.prepareUiweightingDialog)
weightingdialog.weightingDataObrained.connect(confirmdialog.prepareUiCofirmDlg)
confirmdialog.weightingAcceptedSignal.connect(write_changes_to_database)
confirmdialog.weightingAcceptedSignal.connect(finishdialog.prepareUiFinishDlg)
finishdialog.restartTriggered.connect(rfiddialog.prepareUI)
confirmdialog.needReweightingSignal.connect(reweightingreasondialog.show)
reweightingreasondialog.reweightingReasonOptained.connect(write_info_about_reweighting)
reweightingreasondialog.reweightingReasonOptained.connect(weightingdialog.reweighting)

rfiddialog.show()
app.exec_()



