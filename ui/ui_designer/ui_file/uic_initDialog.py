# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initDialog(object):
    def setupUi(self, initDialog):
        initDialog.setObjectName("initDialog")
        initDialog.resize(450, 180)
        initDialog.setMinimumSize(QtCore.QSize(450, 180))
        initDialog.setMaximumSize(QtCore.QSize(450, 180))
        self.txtUserName = QtWidgets.QLineEdit(initDialog)
        self.txtUserName.setGeometry(QtCore.QRect(130, 20, 291, 31))
        self.txtUserName.setObjectName("txtUserName")
        self.lblUserName = QtWidgets.QLabel(initDialog)
        self.lblUserName.setGeometry(QtCore.QRect(20, 26, 90, 16))
        self.lblUserName.setObjectName("lblUserName")
        self.lblPlayerPath = QtWidgets.QLabel(initDialog)
        self.lblPlayerPath.setGeometry(QtCore.QRect(20, 69, 156, 16))
        self.lblPlayerPath.setObjectName("lblPlayerPath")
        self.lblIDMPath = QtWidgets.QLabel(initDialog)
        self.lblIDMPath.setGeometry(QtCore.QRect(20, 110, 156, 16))
        self.lblIDMPath.setObjectName("lblIDMPath")
        self.btnChoosePlayer = QtWidgets.QToolButton(initDialog)
        self.btnChoosePlayer.setGeometry(QtCore.QRect(190, 69, 37, 18))
        self.btnChoosePlayer.setObjectName("btnChoosePlayer")
        self.btnChooseIDM = QtWidgets.QToolButton(initDialog)
        self.btnChooseIDM.setGeometry(QtCore.QRect(190, 110, 37, 18))
        self.btnChooseIDM.setObjectName("btnChooseIDM")
        self.lblPlayer = QtWidgets.QLabel(initDialog)
        self.lblPlayer.setGeometry(QtCore.QRect(240, 69, 181, 16))
        self.lblPlayer.setObjectName("lblPlayer")
        self.lblIDM = QtWidgets.QLabel(initDialog)
        self.lblIDM.setGeometry(QtCore.QRect(240, 110, 181, 16))
        self.lblIDM.setObjectName("lblIDM")
        self.btnFinished = QtWidgets.QPushButton(initDialog)
        self.btnFinished.setGeometry(QtCore.QRect(340, 140, 75, 31))
        self.btnFinished.setObjectName("btnFinished")

        self.retranslateUi(initDialog)
        QtCore.QMetaObject.connectSlotsByName(initDialog)

    def retranslateUi(self, initDialog):
        _translate = QtCore.QCoreApplication.translate
        initDialog.setWindowTitle(_translate("initDialog", "做一些初始化"))
        self.lblUserName.setText(_translate("initDialog", "用户名(8个字符)"))
        self.lblPlayerPath.setText(_translate("initDialog", "播放器路径(可以暂时不选择)"))
        self.lblIDMPath.setText(_translate("initDialog", "下载器路径(可以暂时不选择)"))
        self.btnChoosePlayer.setText(_translate("initDialog", "..."))
        self.btnChooseIDM.setText(_translate("initDialog", "..."))
        self.lblPlayer.setText(_translate("initDialog", "无"))
        self.lblIDM.setText(_translate("initDialog", "无"))
        self.btnFinished.setText(_translate("initDialog", "完成"))
