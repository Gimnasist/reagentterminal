#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *
import finishedDialog_ui


class finishedDlg(QDialog, finishedDialog_ui.Ui_finishedDialog):
    """MainWindow inherits QMainWindow"""
    restartTriggered=pyqtSignal()

    def __init__(self, parent=None):
        super(finishedDlg, self).__init__(parent)
        self.ui = finishedDialog_ui.Ui_finishedDialog()
        self.ui.setupUi(self)
        self.seconds_remain=20
        self.timertoactivatebutton=QTimer()
        self.timertoactivatebutton.timeout.connect(self.repaintLabel)

    def __del__(self):
        self.ui = None

    def repaintLabel(self):
        if self.seconds_remain>=0:
            self.ui.countToActivateRestartLabel.setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">"+str(self.seconds_remain)+"</span></p></body></html>")
            self.seconds_remain-=1
        else:
            self.timertoactivatebutton.stop()
            self.ui.restartPushButton.setEnabled(True)

    def on_restartPushButton_pressed(self):
        self.restartTriggered.emit()
        self.hide()

    def prepareUiFinishDlg(self, barcodedialogpointer):
        self.seconds_remain=20
        self.timertoactivatebutton.start(1000)
        self.ui.storagePlaceLabel.setText(barcodedialogpointer.weightingDLGPointer.reag_storage)
        self.ui.restartPushButton.setEnabled(False)
        self.show()

    # def on_weightLineEdit_returnPressed(self):
    #     print("Weitings are optained")


#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('reagentterminal')
    style = QStyleFactory.create('GTK+')
    app.setStyle(style)

    # create widget
    w =finishedDlg()
    w.setWindowTitle('reagentterminal')
    w.exec_()

    # connection
    app.lastWindowClosed.connect(quit())

    # execute application
    sys.exit(app.exec_())