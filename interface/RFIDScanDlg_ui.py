# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RFIDScanDlg.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RFIDScanDlg(object):
    def setupUi(self, RFIDScanDlg):
        RFIDScanDlg.setObjectName("RFIDScanDlg")
        RFIDScanDlg.resize(480, 320)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RFIDScanDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(RFIDScanDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.instructionLabel = QtWidgets.QLabel(RFIDScanDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instructionLabel.setFont(font)
        self.instructionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout.addWidget(self.instructionLabel)
        self.RFIDidLineEdit = QtWidgets.QLineEdit(RFIDScanDlg)
        self.RFIDidLineEdit.setObjectName("RFIDidLineEdit")
        self.verticalLayout.addWidget(self.RFIDidLineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.logoLabel = QtWidgets.QLabel(RFIDScanDlg)
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/Icons/uflogo.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.verticalLayout_2.addWidget(self.logoLabel)

        self.retranslateUi(RFIDScanDlg)
        QtCore.QMetaObject.connectSlotsByName(RFIDScanDlg)

    def retranslateUi(self, RFIDScanDlg):
        _translate = QtCore.QCoreApplication.translate
        RFIDScanDlg.setWindowTitle(_translate("RFIDScanDlg", "Reagents and hardware - Step 1"))
        self.headerLabel.setText(_translate("RFIDScanDlg", "Система обліку реактивів та обладнання"))
        self.instructionLabel.setText(_translate("RFIDScanDlg", "Будь ласка, відскануйте вашу перепустку <br> (RFID-картку), <br>щоб розпочати транзакцію:"))
        self.RFIDidLineEdit.setToolTip(_translate("RFIDScanDlg", "<html><head/><body><p>Ви можете ввести номер картки вручну, якщо сканер RFID не працює! Після завершення введення натисніть <span style=\" font-weight:600;\">ENTER</span></p></body></html>"))

    def getoperatorrfid(self,RFIDScanDlg):
        return self.RFIDidLineEdit.text()
import reagentterminal_rc
