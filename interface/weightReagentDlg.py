#!-*-coding:utf-8-*-
import sys
import time
# import PyQt4 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import *
import weightReagent_ui
from mainclasses_rdb import *


class weightReagentDlg(QDialog, weightReagent_ui.Ui_weightReagentDlg):
    """MainWindow inherits QMainWindow"""
    weightingDataObrained=pyqtSignal(QDialog)

    def __init__(self, parent=None):
        super(weightReagentDlg,self).__init__(parent)
        self.ui = weightReagent_ui.Ui_weightReagentDlg()
        self.ui.setupUi(self)
        self.optainedWeighting=None
        self.current_scales=Scales('FTDI')
        self.weightingeventtrigger=QTimer()
        self.weightingeventtrigger.timeout.connect(self.optainWeight)

    def __del__(self):
        self.ui = None

    def optainWeight(self):
        self.optainedWeighting=self.current_scales.readWeightFromScale()
        if self.optainedWeighting is not None:
            self.weightingeventtrigger.stop()
            print (self.optainedWeighting, "Weitings was optained by scale")
            self.weightingDataObrained.emit(self)
            self.hide()

    def on_weightLineEdit_returnPressed(self):
        self.weightingeventtrigger.stop()
        self.optainedWeighting=str(float(self.ui.weightLineEdit.text())*1000)
        self.current_scales.notred=False
        print (self.optainedWeighting, "Weitings are optained by hand")
        self.weightingDataObrained.emit(self)
        self.hide()

    def prepareUiweightingDialog(self, barcodedialogpointer):
        self.reag_name=barcodedialogpointer.get_reagent_name_local()
        self.reag_group=barcodedialogpointer.current_reagent.get_reagent_group()
        self.reag_exp_date=barcodedialogpointer.current_reagent.get_exp_date().toString('yyyy-MM-dd')
        self.reag_amount=barcodedialogpointer.current_reagent.get_amount()
        self.current_operator_name=barcodedialogpointer.current_operator_name
        self.reag_storage=barcodedialogpointer.current_reagent.get_storage_place()
        if barcodedialogpointer is not None:
            self.ui.selectedReagentLabel.setText(self.reag_name)
            self.ui.reagentTypeLabel.setText(self.reag_group)
            self.ui.expDateLabel.setText(self.reag_exp_date)
            self.ui.availableAmountLabel.setText(str(self.reag_amount)+ ' mg')
            self.ui.operatorNameHolders3.setText(self.current_operator_name)
        self.ui.weightLineEdit.clear()
        self.optainedWeighting=None
        self.show()
        self.weightingeventtrigger.start(75)

    def reweighting(self):
        self.ui.weightLineEdit.clear()
        self.optainedWeighting=None
        self.show()
        self.weightingeventtrigger.start(75)


#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('reagentterminal')
    style=QStyleFactory.create('GTK+')
    app.setStyle(style)

    # create widget
    w = weightReagentDlg()
    w.setWindowTitle('reagentterminal')
    w.exec_()

    # connection
    app.lastWindowClosed.connect(quit())

    # execute application
    sys.exit(app.exec_())

