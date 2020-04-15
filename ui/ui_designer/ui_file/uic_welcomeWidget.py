# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcomeWidget(object):
    def setupUi(self, welcomeWidget):
        welcomeWidget.setObjectName("welcomeWidget")
        welcomeWidget.resize(984, 519)
        self.lblGif = QtWidgets.QLabel(welcomeWidget)
        self.lblGif.setGeometry(QtCore.QRect(0, 420, 100, 100))
        self.lblGif.setMinimumSize(QtCore.QSize(100, 100))
        self.lblGif.setMaximumSize(QtCore.QSize(100, 100))
        self.lblGif.setStyleSheet("")
        self.lblGif.setText("")
        self.lblGif.setObjectName("lblGif")
        self.widgetDateTime = QtWidgets.QWidget(welcomeWidget)
        self.widgetDateTime.setGeometry(QtCore.QRect(650, 20, 315, 100))
        self.widgetDateTime.setMinimumSize(QtCore.QSize(315, 100))
        self.widgetDateTime.setMaximumSize(QtCore.QSize(315, 100))
        self.widgetDateTime.setStyleSheet("background-color: rgba(0, 0, 0, 84);")
        self.widgetDateTime.setObjectName("widgetDateTime")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetDateTime)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDate = QtWidgets.QLabel(self.widgetDateTime)
        self.lblDate.setStyleSheet("font: 28pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDate.setObjectName("lblDate")
        self.verticalLayout.addWidget(self.lblDate)
        self.lblTime = QtWidgets.QLabel(self.widgetDateTime)
        self.lblTime.setStyleSheet("font: 28pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        self.verticalLayout.addWidget(self.lblTime)
        self.widget = QtWidgets.QWidget(welcomeWidget)
        self.widget.setGeometry(QtCore.QRect(20, 320, 471, 181))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 84);")
        self.widget.setObjectName("widget")
        self.lblDate_4 = QtWidgets.QLabel(self.widget)
        self.lblDate_4.setGeometry(QtCore.QRect(20, 70, 441, 101))
        self.lblDate_4.setStyleSheet("font: 28pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblDate_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblDate_4.setObjectName("lblDate_4")
        self.lblDate_3 = QtWidgets.QLabel(self.widget)
        self.lblDate_3.setGeometry(QtCore.QRect(20, 20, 291, 51))
        self.lblDate_3.setStyleSheet("font: 28pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblDate_3.setObjectName("lblDate_3")

        self.retranslateUi(welcomeWidget)
        QtCore.QMetaObject.connectSlotsByName(welcomeWidget)

    def retranslateUi(self, welcomeWidget):
        _translate = QtCore.QCoreApplication.translate
        welcomeWidget.setWindowTitle(_translate("welcomeWidget", "Form"))
        self.lblDate.setText(_translate("welcomeWidget", "2020年04月15日"))
        self.lblTime.setText(_translate("welcomeWidget", "11:11:11"))
        self.lblDate_4.setText(_translate("welcomeWidget", "今天想要看点什么呢？\n"
"我这里什么都有哦！(大概)"))
        self.lblDate_3.setText(_translate("welcomeWidget", "下午好 Tanyiqu！"))
