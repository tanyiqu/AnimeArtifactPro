# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logsForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_logsForm(object):
    def setupUi(self, logsForm):
        logsForm.setObjectName("logsForm")
        logsForm.resize(300, 350)
        self.gridLayout = QtWidgets.QGridLayout(logsForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(logsForm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 348))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layout.setObjectName("layout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(logsForm)
        QtCore.QMetaObject.connectSlotsByName(logsForm)

    def retranslateUi(self, logsForm):
        _translate = QtCore.QCoreApplication.translate
        logsForm.setWindowTitle(_translate("logsForm", "更新日志"))
