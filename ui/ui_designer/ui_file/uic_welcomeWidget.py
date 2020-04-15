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
        self.lblDate = QtWidgets.QLabel(welcomeWidget)
        self.lblDate.setGeometry(QtCore.QRect(670, 40, 281, 71))
        self.lblDate.setStyleSheet("font: 28pt \"微软雅黑\";")
        self.lblDate.setObjectName("lblDate")
        self.lblGif = QtWidgets.QLabel(welcomeWidget)
        self.lblGif.setGeometry(QtCore.QRect(0, 420, 100, 100))
        self.lblGif.setMinimumSize(QtCore.QSize(100, 100))
        self.lblGif.setMaximumSize(QtCore.QSize(100, 100))
        self.lblGif.setStyleSheet("")
        self.lblGif.setText("")
        self.lblGif.setObjectName("lblGif")
        self.lblTime = QtWidgets.QLabel(welcomeWidget)
        self.lblTime.setGeometry(QtCore.QRect(670, 100, 261, 71))
        self.lblTime.setStyleSheet("font: 28pt \"微软雅黑\";")
        self.lblTime.setObjectName("lblTime")
        self.lblDate_3 = QtWidgets.QLabel(welcomeWidget)
        self.lblDate_3.setGeometry(QtCore.QRect(220, 140, 361, 51))
        self.lblDate_3.setStyleSheet("font: 28pt \"微软雅黑\";")
        self.lblDate_3.setObjectName("lblDate_3")
        self.lblDate_4 = QtWidgets.QLabel(welcomeWidget)
        self.lblDate_4.setGeometry(QtCore.QRect(220, 190, 501, 131))
        self.lblDate_4.setStyleSheet("font: 28pt \"微软雅黑\";")
        self.lblDate_4.setObjectName("lblDate_4")

        self.retranslateUi(welcomeWidget)
        QtCore.QMetaObject.connectSlotsByName(welcomeWidget)

    def retranslateUi(self, welcomeWidget):
        _translate = QtCore.QCoreApplication.translate
        welcomeWidget.setWindowTitle(_translate("welcomeWidget", "Form"))
        self.lblDate.setText(_translate("welcomeWidget", "2020年4月15日"))
        self.lblTime.setText(_translate("welcomeWidget", "13:34"))
        self.lblDate_3.setText(_translate("welcomeWidget", "下午好 Tanyiqu"))
        self.lblDate_4.setText(_translate("welcomeWidget", "今天想要看点什么呢？\n"
"我这里什么都有哦！(大概)"))
