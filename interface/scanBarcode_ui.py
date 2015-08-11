# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanBarcode.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_barcodeScanDlg(object):
    def setupUi(self, barcodeScanDlg):
        barcodeScanDlg.setObjectName("barcodeScanDlg")
        barcodeScanDlg.resize(480, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(barcodeScanDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(barcodeScanDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.headerLabel.setFont(font)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.operatorLabels2 = QtWidgets.QLabel(barcodeScanDlg)
        self.operatorLabels2.setObjectName("operatorLabels2")
        self.horizontalLayout_4.addWidget(self.operatorLabels2)
        self.operatorNameHolder = QtWidgets.QLabel(barcodeScanDlg)
        self.operatorNameHolder.setObjectName("operatorNameHolder")
        self.horizontalLayout_4.addWidget(self.operatorNameHolder)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.instructionLabel = QtWidgets.QLabel(barcodeScanDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instructionLabel.setFont(font)
        self.instructionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout.addWidget(self.instructionLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EANLabel = QtWidgets.QLabel(barcodeScanDlg)
        self.EANLabel.setObjectName("EANLabel")
        self.horizontalLayout.addWidget(self.EANLabel)
        self.eanImageLabel = QtWidgets.QLabel(barcodeScanDlg)
        self.eanImageLabel.setText("")
        self.eanImageLabel.setPixmap(QtGui.QPixmap(":/Icons/ean.png"))
        self.eanImageLabel.setObjectName("eanImageLabel")
        self.horizontalLayout.addWidget(self.eanImageLabel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dataMatrixLabel = QtWidgets.QLabel(barcodeScanDlg)
        self.dataMatrixLabel.setObjectName("dataMatrixLabel")
        self.horizontalLayout_2.addWidget(self.dataMatrixLabel)
        self.dataMatrixImageLabel = QtWidgets.QLabel(barcodeScanDlg)
        self.dataMatrixImageLabel.setText("")
        self.dataMatrixImageLabel.setPixmap(QtGui.QPixmap(":/Icons/datamatrix.png"))
        self.dataMatrixImageLabel.setObjectName("dataMatrixImageLabel")
        self.horizontalLayout_2.addWidget(self.dataMatrixImageLabel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.barcodeLineEdit = QtWidgets.QLineEdit(barcodeScanDlg)
        self.barcodeLineEdit.setObjectName("barcodeLineEdit")
        self.verticalLayout.addWidget(self.barcodeLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(17, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.logoLabel = QtWidgets.QLabel(barcodeScanDlg)
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/Icons/uflogo.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.verticalLayout.addWidget(self.logoLabel)

        self.retranslateUi(barcodeScanDlg)
        QtCore.QMetaObject.connectSlotsByName(barcodeScanDlg)

    def retranslateUi(self, barcodeScanDlg):
        _translate = QtCore.QCoreApplication.translate
        barcodeScanDlg.setWindowTitle(_translate("barcodeScanDlg", "Reagents and hardware - Step 2"))
        self.headerLabel.setText(_translate("barcodeScanDlg", "Система обліку реактивів та обладнання"))
        self.operatorLabels2.setText(_translate("barcodeScanDlg", "Оператор:"))
        self.operatorNameHolder.setText(_translate("barcodeScanDlg", "NA (не доступно)"))
        self.instructionLabel.setText(_translate("barcodeScanDlg", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">Відскануйте штрих-код (EAN або DataMatrix) </span></p><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">на ємності з реактивом:</span></p></body></html>"))
        self.EANLabel.setText(_translate("barcodeScanDlg", "EAN:"))
        self.dataMatrixLabel.setText(_translate("barcodeScanDlg", "DataMatrix"))
        self.barcodeLineEdit.setToolTip(_translate("barcodeScanDlg", "<html><head/><body><p><span style=\" font-size:8pt;\">Ви можете ввести штрих-код вручну, якщо не маєте можливості відсканувати. Після заврешення вводу натисніть </span><span style=\" font-size:8pt; font-weight:600;\">ENTER</span></p></body></html>"))

    def setOperatorName(self,operatorNameString):
        self.operatorNameHolder.setText(operatorNameString)

import reagentterminal_rc
