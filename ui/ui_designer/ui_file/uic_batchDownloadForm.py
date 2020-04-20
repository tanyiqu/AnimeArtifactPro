# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batchDownloadForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_batchDownloadForm(object):
    def setupUi(self, batchDownloadForm):
        batchDownloadForm.setObjectName("batchDownloadForm")
        batchDownloadForm.resize(330, 150)
        batchDownloadForm.setMinimumSize(QtCore.QSize(330, 140))
        batchDownloadForm.setMaximumSize(QtCore.QSize(330, 150))
        self.label = QtWidgets.QLabel(batchDownloadForm)
        self.label.setGeometry(QtCore.QRect(10, 15, 51, 16))
        self.label.setObjectName("label")
        self.btnChooseDir = QtWidgets.QToolButton(batchDownloadForm)
        self.btnChooseDir.setGeometry(QtCore.QRect(70, 15, 37, 18))
        self.btnChooseDir.setObjectName("btnChooseDir")
        self.lblDir = QtWidgets.QLabel(batchDownloadForm)
        self.lblDir.setGeometry(QtCore.QRect(120, 17, 191, 55))
        self.lblDir.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblDir.setWordWrap(True)
        self.lblDir.setObjectName("lblDir")
        self.label_3 = QtWidgets.QLabel(batchDownloadForm)
        self.label_3.setGeometry(QtCore.QRect(10, 83, 311, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.btnOK = QtWidgets.QPushButton(batchDownloadForm)
        self.btnOK.setGeometry(QtCore.QRect(240, 120, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.btnCheckIDM = QtWidgets.QPushButton(batchDownloadForm)
        self.btnCheckIDM.setGeometry(QtCore.QRect(80, 120, 75, 23))
        self.btnCheckIDM.setObjectName("btnCheckIDM")
        self.btnCheckLinks = QtWidgets.QPushButton(batchDownloadForm)
        self.btnCheckLinks.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.btnCheckLinks.setObjectName("btnCheckLinks")

        self.retranslateUi(batchDownloadForm)
        QtCore.QMetaObject.connectSlotsByName(batchDownloadForm)

    def retranslateUi(self, batchDownloadForm):
        _translate = QtCore.QCoreApplication.translate
        batchDownloadForm.setWindowTitle(_translate("batchDownloadForm", "批量下载"))
        self.label.setText(_translate("batchDownloadForm", "选择路径"))
        self.btnChooseDir.setText(_translate("batchDownloadForm", "..."))
        self.lblDir.setText(_translate("batchDownloadForm", "无"))
        self.label_3.setText(_translate("batchDownloadForm", "注：在点击下载前，请务必确保自己配置的IDM是有效的！\n"
"桌面上一定要有已抓取的download.txt文件"))
        self.btnOK.setText(_translate("batchDownloadForm", "确定"))
        self.btnCheckIDM.setText(_translate("batchDownloadForm", "检查IDM"))
        self.btnCheckLinks.setText(_translate("batchDownloadForm", "检查链接"))
