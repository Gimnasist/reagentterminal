#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import scanBarcode_ui
from mainclasses_rdb import *


class scanBarcodeDlg(QDialog, scanBarcode_ui.Ui_barcodeScanDlg):
    """MainWindow inherits QMainWindow"""
    reagentDataOptained=pyqtSignal(QDialog)

    def __init__(self, parent=None):
        super(scanBarcodeDlg,self).__init__(parent)
        self.ui = scanBarcode_ui.Ui_barcodeScanDlg()
        self.ui.setupUi(self)
        self.scannedbarcode=None
        self.current_reagent=None

    def __del__(self):
        self.ui = None

    def on_barcodeLineEdit_returnPressed(self):
        self.scannedbarcode=self.ui.barcodeLineEdit.text()
        self.current_reagent=Reagent(self.scannedbarcode)
        self.reagentDataOptained.emit(self)
        print (self.scannedbarcode,"Autoconnection of slots succeed")
        self.hide()

    def prepareUIscanBarcodeDlg(self, operator_name_string):
        self.current_operator_name=operator_name_string
        self.ui.setOperatorName(operator_name_string)
        self.scannedbarcode=None
        self.current_reagent=None
        self.ui.barcodeLineEdit.clear()
        self.show()

    def get_reagent_name_local(self):
        if self.current_reagent is not None:
            return self.current_reagent.get_reagent_name()

#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('reagentterminal')
    style=QStyleFactory.create('GTK+')
    app.setStyle(style)

    # create widget
    w = scanBarcodeDlg()
    w.setWindowTitle('reagentterminal')
    w.exec_()

    # connection
    app.lastWindowClosed.connect(quit())

    # execute application
    sys.exit(app.exec_())

