#!-*-coding:utf-8-*-
import sys
import time

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *
import confirmDlg_ui


class confirmDlg(QDialog, confirmDlg_ui.Ui_confirmDlg):
    """MainWindow inherits QMainWindow"""
    timeToAutoacceptElapsed=pyqtSignal()
    weightingAcceptedSignal=pyqtSignal(QDialog)
    needReweightingSignal=pyqtSignal()

    def __init__(self, parent=None):
        super(confirmDlg, self).__init__(parent)
        self.ui = confirmDlg_ui.Ui_confirmDlg()
        self.ui.setupUi(self)
        self.seconds_remain=10
        self.timertoaccept=QTimer()
        self.timertoaccept.timeout.connect(self.repaintLabel)

    def __del__(self):
        self.ui = None

    def weightingaccepted(self):
        self.weightingAcceptedSignal.emit(self)
        print ('accept')
        self.hide()

    def needreweight(self):
        self.needReweightingSignal.emit()
        print ('reweight')
        self.hide()

    def on_acceptPushButton_pressed(self):
        self.timertoaccept.stop()
        self.weightingaccepted()

    def on_reweightPushButton_pressed(self):
        self.timertoaccept.stop()
        self.needreweight()

    def repaintLabel(self):
        if self.seconds_remain>=0:
            self.ui.countdownLabel.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">"+str(self.seconds_remain)+"</span></p></body></html>")
            self.seconds_remain-=1
        else:
            self.timertoaccept.stop()
            self.weightingaccepted()

    def prepareUiCofirmDlg(self, weightdialogpointer):
        self.weightingDLGPointer=weightdialogpointer
        if weightdialogpointer is not None:
            self.ui.operatorNameHolders4.setText(weightdialogpointer.current_operator_name)
            self.ui.selectedReagentLabel.setText(weightdialogpointer.reag_name)
            self.ui.expirationDateLabel.setText(weightdialogpointer.reag_exp_date)
            self.ui.weightedAmountLabel.setText(weightdialogpointer.optainedWeighting+' mg')
        self.show()
        self.seconds_remain=10
        self.timertoaccept.start(1000)



#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('reagentterminal')
    style = QStyleFactory.create('fusion')
    app.setStyle(style)

    # create widget
    w = confirmDlg()
    w.setWindowTitle('reagentterminal')
    w.exec_()

    # connection
    app.lastWindowClosed.connect(quit())

    # execute application
    sys.exit(app.exec_())