# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reweightingReasonDlg.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reweightingReasonDlg(object):
    def setupUi(self, reweightingReasonDlg):
        reweightingReasonDlg.setObjectName("reweightingReasonDlg")
        reweightingReasonDlg.resize(480, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(reweightingReasonDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(reweightingReasonDlg)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.instructionLabel = QtWidgets.QLabel(reweightingReasonDlg)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout.addWidget(self.instructionLabel)
        self.wrongWeightingPushButton = QtWidgets.QPushButton(reweightingReasonDlg)
        self.wrongWeightingPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.wrongWeightingPushButton.setObjectName("wrongWeightingPushButton")
        self.verticalLayout.addWidget(self.wrongWeightingPushButton)
        self.recalculationPushButton = QtWidgets.QPushButton(reweightingReasonDlg)
        self.recalculationPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.recalculationPushButton.setObjectName("recalculationPushButton")
        self.verticalLayout.addWidget(self.recalculationPushButton)
        self.untaredPushButton = QtWidgets.QPushButton(reweightingReasonDlg)
        self.untaredPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.untaredPushButton.setObjectName("untaredPushButton")
        self.verticalLayout.addWidget(self.untaredPushButton)
        self.incorrectReagentPushButton = QtWidgets.QPushButton(reweightingReasonDlg)
        self.incorrectReagentPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.incorrectReagentPushButton.setObjectName("incorrectReagentPushButton")
        self.verticalLayout.addWidget(self.incorrectReagentPushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ownReasonLabel = QtWidgets.QLabel(reweightingReasonDlg)
        self.ownReasonLabel.setObjectName("ownReasonLabel")
        self.horizontalLayout.addWidget(self.ownReasonLabel)
        self.ownReasonLineEdit = QtWidgets.QLineEdit(reweightingReasonDlg)
        self.ownReasonLineEdit.setObjectName("ownReasonLineEdit")
        self.horizontalLayout.addWidget(self.ownReasonLineEdit)
        self.ownReasonAcceptPushButton = QtWidgets.QPushButton(reweightingReasonDlg)
        self.ownReasonAcceptPushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.ownReasonAcceptPushButton.setObjectName("ownReasonAcceptPushButton")
        self.horizontalLayout.addWidget(self.ownReasonAcceptPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.logoLabel = QtWidgets.QLabel(reweightingReasonDlg)
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/Icons/uflogo.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.verticalLayout.addWidget(self.logoLabel)

        self.retranslateUi(reweightingReasonDlg)
        QtCore.QMetaObject.connectSlotsByName(reweightingReasonDlg)

    def retranslateUi(self, reweightingReasonDlg):
        _translate = QtCore.QCoreApplication.translate
        reweightingReasonDlg.setWindowTitle(_translate("reweightingReasonDlg", "Reweighting reason"))
        self.headerLabel.setText(_translate("reweightingReasonDlg", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Виберіть причину переважування</span></p></body></html>"))
        self.instructionLabel.setText(_translate("reweightingReasonDlg", "<html><head/><body><p align=\"center\">Якщо ваша причина відсутня в списку, <br/>введіть її в поле нижче та натисніть ОК</p></body></html>"))
        self.wrongWeightingPushButton.setText(_translate("reweightingReasonDlg", "Невірна наважка"))
        self.recalculationPushButton.setText(_translate("reweightingReasonDlg", "Перерахунок необхідної кількості реактиву"))
        self.untaredPushButton.setText(_translate("reweightingReasonDlg", "Незатарений посуд"))
        self.incorrectReagentPushButton.setText(_translate("reweightingReasonDlg", "Невірний реактив"))
        self.ownReasonLabel.setText(_translate("reweightingReasonDlg", "Власна причина:"))
        self.ownReasonAcceptPushButton.setText(_translate("reweightingReasonDlg", "OK"))

import reagentterminal_rc
