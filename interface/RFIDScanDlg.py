#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *
import RFIDScanDlg_ui
from mainclasses_rdb import *


class RFIDScanDlg(QDialog, RFIDScanDlg_ui.Ui_RFIDScanDlg):
    """MainWindow inherits QMainWindow"""
    rfidCodeObtained=pyqtSignal(str)

    def __init__(self, parent=None):
        super(RFIDScanDlg,self).__init__(parent)
        self.ui = RFIDScanDlg_ui.Ui_RFIDScanDlg()
        self.ui.setupUi(self)
        self.current_operator=None
        self.current_operator_full_name=None
        self.operator_rfid_code=None

    def __del__(self):
        self.ui = None

    def on_RFIDidLineEdit_returnPressed(self):
        self.operator_rfid_code=self.ui.getoperatorrfid(self)
        self.current_operator=Operator(self.operator_rfid_code)
        self.current_operator_full_name=self.current_operator.get_operator_full_name()
        del self.current_operator
        print (self.current_operator_full_name, self.operator_rfid_code, "RFID code is optained")
        self.rfidCodeObtained.emit(self.current_operator_full_name)
        self.hide()

    def prepareUI(self):
        self.current_operator=None
        self.current_operator_full_name=None
        self.operator_rfid_code=None
        self.ui.RFIDidLineEdit.clear()
        self.show()

#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('reagentterminal')
    style=QStyleFactory.create('GTK+')
    app.setStyle(style)

    # create widget
    w = RFIDScanDlg()
    w.setWindowTitle('reagentterminal')
    w.exec_()

    # connection
    app.lastWindowClosed.connect(quit())

    # execute application
    sys.exit(app.exec_())

