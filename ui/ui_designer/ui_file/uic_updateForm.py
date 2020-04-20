# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_updateForm(object):
    def setupUi(self, updateForm):
        updateForm.setObjectName("updateForm")
        updateForm.resize(240, 100)
        updateForm.setMinimumSize(QtCore.QSize(240, 100))
        updateForm.setMaximumSize(QtCore.QSize(240, 100))
        self.label = QtWidgets.QLabel(updateForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.label.setObjectName("label")
        self.btnGet = QtWidgets.QPushButton(updateForm)
        self.btnGet.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.btnGet.setObjectName("btnGet")
        self.btnMore = QtWidgets.QPushButton(updateForm)
        self.btnMore.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.btnMore.setObjectName("btnMore")

        self.retranslateUi(updateForm)
        QtCore.QMetaObject.connectSlotsByName(updateForm)

    def retranslateUi(self, updateForm):
        _translate = QtCore.QCoreApplication.translate
        updateForm.setWindowTitle(_translate("updateForm", "版本更新"))
        self.label.setText(_translate("updateForm", "貌似有新版本了"))
        self.btnGet.setText(_translate("updateForm", "获取"))
        self.btnMore.setText(_translate("updateForm", "新版说明"))
