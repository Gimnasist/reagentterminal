# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finishedDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_finishedDialog(object):
    def setupUi(self, finishedDialog):
        finishedDialog.setObjectName("finishedDialog")
        finishedDialog.resize(480, 320)
        finishedDialog.setMaximumSize(QtCore.QSize(480, 320))
        self.verticalLayout = QtWidgets.QVBoxLayout(finishedDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(finishedDialog)
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.instructionLabel = QtWidgets.QLabel(finishedDialog)
        self.instructionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionLabel.setObjectName("instructionLabel")
        self.verticalLayout.addWidget(self.instructionLabel)
        self.storagePlaceLabel = QtWidgets.QLabel(finishedDialog)
        self.storagePlaceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.storagePlaceLabel.setObjectName("storagePlaceLabel")
        self.verticalLayout.addWidget(self.storagePlaceLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.instruction3Label = QtWidgets.QLabel(finishedDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instruction3Label.setFont(font)
        self.instruction3Label.setObjectName("instruction3Label")
        self.horizontalLayout.addWidget(self.instruction3Label)
        self.countToActivateRestartLabel = QtWidgets.QLabel(finishedDialog)
        self.countToActivateRestartLabel.setObjectName("countToActivateRestartLabel")
        self.horizontalLayout.addWidget(self.countToActivateRestartLabel)
        self.instruction2Label = QtWidgets.QLabel(finishedDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instruction2Label.setFont(font)
        self.instruction2Label.setObjectName("instruction2Label")
        self.horizontalLayout.addWidget(self.instruction2Label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.restartPushButton = QtWidgets.QPushButton(finishedDialog)
        self.restartPushButton.setEnabled(False)
        self.restartPushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.restartPushButton.setObjectName("restartPushButton")
        self.verticalLayout.addWidget(self.restartPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.logoLabel = QtWidgets.QLabel(finishedDialog)
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap(":/Icons/uflogo.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.verticalLayout.addWidget(self.logoLabel)

        self.retranslateUi(finishedDialog)
        QtCore.QMetaObject.connectSlotsByName(finishedDialog)

    def retranslateUi(self, finishedDialog):
        _translate = QtCore.QCoreApplication.translate
        finishedDialog.setWindowTitle(_translate("finishedDialog", "Reagents and hardware - Finished"))
        self.headerLabel.setText(_translate("finishedDialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Відбір реагента завершено!</span></p></body></html>"))
        self.instructionLabel.setText(_translate("finishedDialog", "<html><head/><body><p align=\"center\">Перемість відібраний реагент до місця зберігання:</p></body></html>"))
        self.storagePlaceLabel.setText(_translate("finishedDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Storage Place</span></p></body></html>"))
        self.instruction3Label.setText(_translate("finishedDialog", "Маєте"))
        self.countToActivateRestartLabel.setText(_translate("finishedDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">NA</span></p></body></html>"))
        self.instruction2Label.setText(_translate("finishedDialog", "сек. для переміщення реактиву на зберігання:)"))
        self.restartPushButton.setText(_translate("finishedDialog", "Відібрати новий реактив"))

import reagentterminal_rc
