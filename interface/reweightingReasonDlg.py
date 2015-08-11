#!-*-coding:utf-8-*-
import sys
import time
# import PyQt4 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *
import reweightingReasonDlg_ui


class reweightingReasonDlg(QDialog, reweightingReasonDlg_ui.Ui_reweightingReasonDlg):
    """MainWindow inherits QMainWindow"""
    reweightingReasonOptained=pyqtSignal(str)

    def __init__(self, parent=None):
        super(reweightingReasonDlg, self).__init__(parent)
        self.ui = reweightingReasonDlg_ui.Ui_reweightingReasonDlg()
        self.ui.setupUi(self)

    def __del__(self):
        self.ui = None

    def on_wrongWeightingPushButton_pressed(self):
        self.reweightingReasonOptained.emit('WRONGWEIGHT')
        self.hide()

    def on_recalculationPushButton_pressed(self):
        self.reweightingReasonOptained.emit('RECALCULATED')
        self.hide()

    def on_untaredPushButton_pressed(self):
        self.reweightingReasonOptained.emit('UNTARED_WEIGHTING')
        self.hide()

    def on_incorrectReagentPushButton_pressed(self):
        self.reweightingReasonOptained.emit('INCORRECT_REAGENT')
        self.hide()

    def on_ownReasonAcceptPushButton_pressed(self):
        self.reweightingReasonOptained.emit(self.ui.ownReasonLineEdit.text())
        self.ui.ownReasonLineEdit.clear()
        self.hide()

    def on_ownReasonLineEdit_returnPressed(self):
        self.reweightingReasonOptained.emit(self.ui.ownReasonLineEdit.text())
        self.ui.ownReasonLineEdit.clear()
        self.hide()


#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('reagentterminal')
    style = QStyleFactory.create('GTK+')
    app.setStyle(style)

    # create widget
    w = reweightingReasonDlg()
    w.setWindowTitle('reagentterminal')
    w.setModal(True)
    w.exec_()

    # connection
    app.lastWindowClosed.connect(quit())

    # execute application
    app.exec_()
