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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(logsForm)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 271, 301))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(logsForm)
        QtCore.QMetaObject.connectSlotsByName(logsForm)

    def retranslateUi(self, logsForm):
        _translate = QtCore.QCoreApplication.translate
        logsForm.setWindowTitle(_translate("logsForm", "更新日志"))
