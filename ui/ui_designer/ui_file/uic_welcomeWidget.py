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
        self.widgetDateTime.setGeometry(QtCore.QRect(340, 100, 315, 100))
        self.widgetDateTime.setMinimumSize(QtCore.QSize(315, 100))
        self.widgetDateTime.setMaximumSize(QtCore.QSize(315, 100))
        self.widgetDateTime.setStyleSheet("background-color: rgba(0, 0, 0, 84);")
        self.widgetDateTime.setObjectName("widgetDateTime")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetDateTime)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDate = QtWidgets.QLabel(self.widgetDateTime)
        self.lblDate.setStyleSheet("font: 25pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDate.setObjectName("lblDate")
        self.verticalLayout.addWidget(self.lblDate)
        self.lblTime = QtWidgets.QLabel(self.widgetDateTime)
        self.lblTime.setStyleSheet("font: 25pt \"黑体\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        self.verticalLayout.addWidget(self.lblTime)
        self.widgetVersion = QtWidgets.QWidget(welcomeWidget)
        self.widgetVersion.setGeometry(QtCore.QRect(340, 200, 315, 51))
        self.widgetVersion.setStyleSheet("background-color: rgba(0, 0, 0, 84);")
        self.widgetVersion.setObjectName("widgetVersion")
        self.lblVersion = QtWidgets.QLabel(self.widgetVersion)
        self.lblVersion.setGeometry(QtCore.QRect(9, 9, 298, 33))
        self.lblVersion.setStyleSheet("font: 25pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblVersion.setObjectName("lblVersion")
        self.widget = QtWidgets.QWidget(welcomeWidget)
        self.widget.setGeometry(QtCore.QRect(298, 251, 401, 141))
        self.widget.setMinimumSize(QtCore.QSize(315, 100))
        self.widget.setMaximumSize(QtCore.QSize(1010, 1010))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 84);")
        self.widget.setObjectName("widget")
        self.lblHello = QtWidgets.QLabel(self.widget)
        self.lblHello.setGeometry(QtCore.QRect(10, 0, 300, 51))
        self.lblHello.setStyleSheet("font: 23pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.lblHello.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblHello.setObjectName("lblHello")
        self.lblHelloWord = QtWidgets.QLabel(self.widget)
        self.lblHelloWord.setGeometry(QtCore.QRect(10, 40, 391, 91))
        self.lblHelloWord.setStyleSheet("font: 23pt \"微软雅黑\";\n"
"color: rgb(236, 236, 236);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblHelloWord.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblHelloWord.setObjectName("lblHelloWord")

        self.retranslateUi(welcomeWidget)
        QtCore.QMetaObject.connectSlotsByName(welcomeWidget)

    def retranslateUi(self, welcomeWidget):
        _translate = QtCore.QCoreApplication.translate
        welcomeWidget.setWindowTitle(_translate("welcomeWidget", "Form"))
        self.lblDate.setText(_translate("welcomeWidget", "2020年04月15日"))
        self.lblTime.setText(_translate("welcomeWidget", "11:11:11"))
        self.lblVersion.setText(_translate("welcomeWidget", "看番神器Pro V1.0"))
        self.lblHello.setText(_translate("welcomeWidget", "下午好 Tanyiqu！"))
        self.lblHelloWord.setText(_translate("welcomeWidget", "今天想要看点什么呢？\n"
"我这里什么都有哦！(大概)"))
