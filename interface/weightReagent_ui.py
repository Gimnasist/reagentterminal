# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weightReagent.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_weightReagentDlg(object):
    def setupUi(self, weightReagentDlg):
        weightReagentDlg.setObjectName("weightReagentDlg")
        weightReagentDlg.resize(480, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(weightReagentDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.operatorNameLabel = QtWidgets.QLabel(weightReagentDlg)
        self.operatorNameLabel.setObjectName("operatorNameLabel")
        self.horizontalLayout_6.addWidget(self.operatorNameLabel)
        self.operatorNameHolders3 = QtWidgets.QLabel(weightReagentDlg)
        self.operatorNameHolders3.setObjectName("operatorNameHolders3")
        self.horizontalLayout_6.addWidget(self.operatorNameHolders3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.srLabel = QtWidgets.QLabel(weightReagentDlg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.srLabel.setFont(font)
        self.srLabel.setObjectName("srLabel")
        self.horizontalLayout.addWidget(self.srLabel)
        self.selectedReagentLabel = QtWidgets.QLabel(weightReagentDlg)
        self.selectedReagentLabel.setObjectName("selectedReagentLabel")
        self.horizontalLayout.addWidget(self.selectedReagentLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rtLabel = QtWidgets.QLabel(weightReagentDlg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rtLabel.setFont(font)
        self.rtLabel.setObjectName("rtLabel")
        self.horizontalLayout_2.addWidget(self.rtLabel)
        self.reagentTypeLabel = QtWidgets.QLabel(weightReagentDlg)
        self.reagentTypeLabel.setObjectName("reagentTypeLabel")
        self.horizontalLayout_2.addWidget(self.reagentTypeLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edLabel = QtWidgets.QLabel(weightReagentDlg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edLabel.setFont(font)
        self.edLabel.setObjectName("edLabel")
        self.horizontalLayout_3.addWidget(self.edLabel)
        self.expDateLabel = QtWidgets.QLabel(weightReagentDlg)
        self.expDateLabel.setObjectName("expDateLabel")
        self.horizontalLayout_3.addWidget(self.expDateLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.aaLabel = QtWidgets.QLabel(weightReagentDlg)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.aaLabel.setFont(font)
        self.aaLabel.setObjectName("aaLabel")
        self.horizontalLayout_4.addWidget(self.aaLabel)
        self.availableAmountLabel = QtWidgets.QLabel(weightReagentDlg)
        self.availableAmountLabel.setObjectName("availableAmountLabel")
        self.horizontalLayout_4.addWidget(self.availableAmountLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(18, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.instructionLabels3 = QtWidgets.QLabel(weightReagentDlg)
        self.instructionLabels3.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionLabels3.setObjectName("instructionLabels3")
        self.verticalLayout.addWidget(self.instructionLabels3)
        self.buttonPreviewLabel = QtWidgets.QLabel(weightReagentDlg)
        self.buttonPreviewLabel.setText("")
        self.buttonPreviewLabel.setPixmap(QtGui.QPixmap(":/Icons/print_button_0.png"))
        self.buttonPreviewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonPreviewLabel.setObjectName("buttonPreviewLabel")
        self.verticalLayout.addWidget(self.buttonPreviewLabel)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.weightLabel = QtWidgets.QLabel(weightReagentDlg)
        self.weightLabel.setObjectName("weightLabel")
        self.horizontalLayout_5.addWidget(self.weightLabel)
        self.weightLineEdit = QtWidgets.QLineEdit(weightReagentDlg)
        self.weightLineEdit.setObjectName("weightLineEdit")
        self.horizontalLayout_5.addWidget(self.weightLineEdit)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(456, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.logoLabel = QtWidgets.QLabel(weightReagentDlg)
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/Icons/uflogo.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.verticalLayout.addWidget(self.logoLabel)

        self.retranslateUi(weightReagentDlg)
        QtCore.QMetaObject.connectSlotsByName(weightReagentDlg)

    def retranslateUi(self, weightReagentDlg):
        _translate = QtCore.QCoreApplication.translate
        weightReagentDlg.setWindowTitle(_translate("weightReagentDlg", "Reagents and hardware - Step 3"))
        self.operatorNameLabel.setText(_translate("weightReagentDlg", "Оператор:"))
        self.operatorNameHolders3.setText(_translate("weightReagentDlg", "NA (не доступно)"))
        self.srLabel.setText(_translate("weightReagentDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Вибраний реагент:</span></p></body></html>"))
        self.selectedReagentLabel.setText(_translate("weightReagentDlg", "NA (не доступно)"))
        self.rtLabel.setText(_translate("weightReagentDlg", "Тип реагенту:"))
        self.reagentTypeLabel.setText(_translate("weightReagentDlg", "NA (не доступно)"))
        self.edLabel.setText(_translate("weightReagentDlg", "Термін придатності:"))
        self.expDateLabel.setText(_translate("weightReagentDlg", "NA (не доступно)"))
        self.aaLabel.setText(_translate("weightReagentDlg", "Доступний залишок:"))
        self.availableAmountLabel.setText(_translate("weightReagentDlg", "NA (не доступно)"))
        self.instructionLabels3.setText(_translate("weightReagentDlg", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Внесіть необхідну наважку на ваги.</span><br/><span style=\" font-size:8pt;\">Після стабілізації маси необхідної наважки </span></p><p align=\"center\"><span style=\" font-size:8pt;\">натисніть на вагах кнопку PRINT:</span></p></body></html>"))
        self.weightLabel.setText(_translate("weightReagentDlg", "Наважка:"))
        self.weightLineEdit.setToolTip(_translate("weightReagentDlg", "<html><head/><body><p>Ви можете ввести наважку вручну, якщо система автоматичної фіксації не спрацювала! Після завершення введення натисніть <span style=\" font-weight:600;\">ENTER</span></p></body></html>"))

import reagentterminal_rc
