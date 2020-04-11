# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_widget_item.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_item(object):
    def setupUi(self, item):
        item.setObjectName("item")
        item.resize(210, 330)
        item.setMinimumSize(QtCore.QSize(210, 330))
        item.setMaximumSize(QtCore.QSize(210, 330))
        item.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.gridLayout = QtWidgets.QGridLayout(item)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblCover = QtWidgets.QLabel(item)
        self.lblCover.setMinimumSize(QtCore.QSize(210, 293))
        self.lblCover.setText("")
        self.lblCover.setObjectName("lblCover")
        self.gridLayout.addWidget(self.lblCover, 0, 0, 1, 1)
        self.lblTitle = QtWidgets.QLabel(item)
        self.lblTitle.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"padding-left:5px")
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 1, 0, 1, 1)

        self.retranslateUi(item)
        QtCore.QMetaObject.connectSlotsByName(item)

    def retranslateUi(self, item):
        _translate = QtCore.QCoreApplication.translate
        item.setWindowTitle(_translate("item", "Form"))
        self.lblTitle.setText(_translate("item", "番名"))
