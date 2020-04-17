# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(341, 388)
        AboutForm.setMinimumSize(QtCore.QSize(341, 388))
        AboutForm.setMaximumSize(QtCore.QSize(341, 388))
        AboutForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logo = QtWidgets.QLabel(AboutForm)
        self.logo.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.lblAppName = QtWidgets.QLabel(AboutForm)
        self.lblAppName.setGeometry(QtCore.QRect(70, 10, 351, 41))
        self.lblAppName.setStyleSheet("font: 17pt \"微软雅黑\";")
        self.lblAppName.setObjectName("lblAppName")
        self.lblVersion_ = QtWidgets.QLabel(AboutForm)
        self.lblVersion_.setGeometry(QtCore.QRect(20, 60, 31, 21))
        self.lblVersion_.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblVersion_.setObjectName("lblVersion_")
        self.lblAuthor_ = QtWidgets.QLabel(AboutForm)
        self.lblAuthor_.setGeometry(QtCore.QRect(20, 80, 31, 21))
        self.lblAuthor_.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblAuthor_.setObjectName("lblAuthor_")
        self.lblVersion = QtWidgets.QLabel(AboutForm)
        self.lblVersion.setGeometry(QtCore.QRect(55, 60, 181, 21))
        self.lblVersion.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblVersion.setObjectName("lblVersion")
        self.lblAuthor = QtWidgets.QLabel(AboutForm)
        self.lblAuthor.setGeometry(QtCore.QRect(55, 80, 311, 21))
        self.lblAuthor.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.lblAuthor.setOpenExternalLinks(True)
        self.lblAuthor.setObjectName("lblAuthor")
        self.gif_1 = QtWidgets.QLabel(AboutForm)
        self.gif_1.setGeometry(QtCore.QRect(0, 290, 100, 100))
        self.gif_1.setText("")
        self.gif_1.setObjectName("gif_1")
        self.content = QtWidgets.QPlainTextEdit(AboutForm)
        self.content.setGeometry(QtCore.QRect(20, 110, 301, 180))
        self.content.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.content.setReadOnly(True)
        self.content.setObjectName("content")
        self.gif_2 = QtWidgets.QLabel(AboutForm)
        self.gif_2.setGeometry(QtCore.QRect(240, 290, 100, 100))
        self.gif_2.setText("")
        self.gif_2.setObjectName("gif_2")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "关于 看番神器"))
        self.lblAppName.setText(_translate("AboutForm", "看番神器 Pro"))
        self.lblVersion_.setText(_translate("AboutForm", "版本"))
        self.lblAuthor_.setText(_translate("AboutForm", "作者"))
        self.lblVersion.setText(_translate("AboutForm", "1.0 (2020.4.12)"))
        self.lblAuthor.setText(_translate("AboutForm", "<a href=https://tanyiqu.github.io>Tanyiqu"))
        self.content.setPlainText(_translate("AboutForm", "看番神器 Pro是由Tanyiqu在2020年4月9日开始独立开发（算不上开发）的一款看动漫的工具软件“看番神器”的基础上进行升级改造的一款看动漫的工具软件。\n"
"新版本在原版的基础上增加了切换接口的功能。\n"
"软件（工具）开源并且完全免费！实际上也没有任何收费的理由。\n"
"软件使用python的爬虫对目标网站进行资源爬取,本人不参与任何上传操作。\n"
"请勿将此工具用于任何非法用途！!\n"
"请勿将此工具用于任何非法用途！!\n"
"请勿将此工具用于任何非法用途！!\n"
"软件的保质期受目标网站的影响，如果目标网站挂掉了可以向我提供更好的网站，我可能会保证此软件的再次使用。\n"
"\n"
"额外感谢：\n"
"● 软件图标：https://www.iconfont.cn/collections/detail?cid=21867\n"
"● 其他：..."))
