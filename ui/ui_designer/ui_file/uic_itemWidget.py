# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemWidget.ui'
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
        item.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        item.setStyleSheet("border: 1px solid #000000;")
        self.gridLayout = QtWidgets.QGridLayout(item)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(item)
        self.widget.setToolTip("")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCover = QtWidgets.QLabel(self.widget)
        self.lblCover.setMinimumSize(QtCore.QSize(210, 300))
        self.lblCover.setStyleSheet("border: 0px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lblCover.setText("")
        self.lblCover.setObjectName("lblCover")
        self.gridLayout_2.addWidget(self.lblCover, 0, 0, 1, 1)
        self.lblLatest = QtWidgets.QLabel(self.widget)
        self.lblLatest.setMinimumSize(QtCore.QSize(0, 30))
        self.lblLatest.setStyleSheet("border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"微软雅黑\";\n"
"padding-right:3px;\n"
"background-color: rgba(0, 0, 0, 128);\n"
"")
        self.lblLatest.setText("")
        self.lblLatest.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLatest.setObjectName("lblLatest")
        self.gridLayout_2.addWidget(self.lblLatest, 1, 0, 1, 1)
        self.lblTitle = QtWidgets.QLabel(self.widget)
        self.lblTitle.setMinimumSize(QtCore.QSize(210, 30))
        self.lblTitle.setMaximumSize(QtCore.QSize(210, 30))
        self.lblTitle.setStyleSheet("font: 11pt \"微软雅黑\";\n"
"padding-left:5px;\n"
"border: 0px;\n"
"color: #ffffff;")
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout_2.addWidget(self.lblTitle, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.retranslateUi(item)
        QtCore.QMetaObject.connectSlotsByName(item)

    def retranslateUi(self, item):
        _translate = QtCore.QCoreApplication.translate
        item.setWindowTitle(_translate("item", "Form"))
        self.lblTitle.setText(_translate("item", "番名"))
