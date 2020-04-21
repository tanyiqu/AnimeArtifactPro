# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(1000, 800)
        mainForm.setMinimumSize(QtCore.QSize(960, 650))
        self.gridMain = QtWidgets.QGridLayout(mainForm)
        self.gridMain.setContentsMargins(8, 8, 8, 8)
        self.gridMain.setSpacing(0)
        self.gridMain.setObjectName("gridMain")
        self.widgetConsole = QtWidgets.QWidget(mainForm)
        self.widgetConsole.setMinimumSize(QtCore.QSize(0, 180))
        self.widgetConsole.setMaximumSize(QtCore.QSize(16777215, 180))
        self.widgetConsole.setObjectName("widgetConsole")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetConsole)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.console1 = QtWidgets.QPlainTextEdit(self.widgetConsole)
        self.console1.setStyleSheet("color: #ffffff;\n"
"background-color: #303038;\n"
"font: 12pt \"微软雅黑\";\n"
"\n"
"\n"
"")
        self.console1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console1.setReadOnly(True)
        self.console1.setPlainText("")
        self.console1.setObjectName("console1")
        self.gridLayout_2.addWidget(self.console1, 0, 0, 1, 1)
        self.console2 = QtWidgets.QPlainTextEdit(self.widgetConsole)
        self.console2.setStyleSheet("color: #ffffff;\n"
"background-color: #303038;\n"
"font: 12pt \"微软雅黑\";\n"
"\n"
"\n"
"")
        self.console2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console2.setReadOnly(True)
        self.console2.setPlainText("")
        self.console2.setObjectName("console2")
        self.gridLayout_2.addWidget(self.console2, 0, 1, 1, 1)
        self.gridMain.addWidget(self.widgetConsole, 3, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(mainForm)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageWelcome = QtWidgets.QWidget()
        self.pageWelcome.setStyleSheet("")
        self.pageWelcome.setObjectName("pageWelcome")
        self.gridWelcome = QtWidgets.QGridLayout(self.pageWelcome)
        self.gridWelcome.setContentsMargins(0, 0, 0, 0)
        self.gridWelcome.setSpacing(0)
        self.gridWelcome.setObjectName("gridWelcome")
        self.stackedWidget.addWidget(self.pageWelcome)
        self.pageSearchResult = QtWidgets.QWidget()
        self.pageSearchResult.setStyleSheet("")
        self.pageSearchResult.setObjectName("pageSearchResult")
        self.gridLayout = QtWidgets.QGridLayout(self.pageSearchResult)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.pageSearchResult)
        self.scrollArea.setStyleSheet("background-color: #303038;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scroll = QtWidgets.QWidget()
        self.scroll.setGeometry(QtCore.QRect(0, 0, 83, 30))
        self.scroll.setObjectName("scroll")
        self.grid = QtWidgets.QGridLayout(self.scroll)
        self.grid.setSpacing(9)
        self.grid.setObjectName("grid")
        self.scrollArea.setWidget(self.scroll)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageSearchResult)
        self.pageDetail = QtWidgets.QWidget()
        self.pageDetail.setStyleSheet("background-color: #303038;")
        self.pageDetail.setObjectName("pageDetail")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.pageDetail)
        self.gridLayout_5.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widgetTop_2 = QtWidgets.QWidget(self.pageDetail)
        self.widgetTop_2.setMinimumSize(QtCore.QSize(0, 300))
        self.widgetTop_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widgetTop_2.setObjectName("widgetTop_2")
        self.widgetDesc = QtWidgets.QWidget(self.widgetTop_2)
        self.widgetDesc.setGeometry(QtCore.QRect(270, 20, 631, 251))
        self.widgetDesc.setStyleSheet("color: #bababa;\n"
"font: 12pt \"微软雅黑\";")
        self.widgetDesc.setObjectName("widgetDesc")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widgetDesc)
        self.gridLayout_7.setContentsMargins(12, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lblTitle = QtWidgets.QLabel(self.widgetDesc)
        self.lblTitle.setMinimumSize(QtCore.QSize(0, 50))
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lblTitle.setStyleSheet("font: 18pt \"微软雅黑\";")
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout_7.addWidget(self.lblTitle, 0, 0, 1, 2)
        self.lblArea = QtWidgets.QLabel(self.widgetDesc)
        self.lblArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblArea.setObjectName("lblArea")
        self.gridLayout_7.addWidget(self.lblArea, 1, 1, 1, 1)
        self.lblTime = QtWidgets.QLabel(self.widgetDesc)
        self.lblTime.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblTime.setObjectName("lblTime")
        self.gridLayout_7.addWidget(self.lblTime, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widgetDesc)
        self.label_5.setMinimumSize(QtCore.QSize(40, 28))
        self.label_5.setMaximumSize(QtCore.QSize(40, 28))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widgetDesc)
        self.label_6.setMinimumSize(QtCore.QSize(0, 28))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widgetDesc)
        self.label_7.setMinimumSize(QtCore.QSize(0, 28))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 2, 0, 1, 1)
        self.lblType = QtWidgets.QLabel(self.widgetDesc)
        self.lblType.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblType.setObjectName("lblType")
        self.gridLayout_7.addWidget(self.lblType, 3, 1, 1, 1)
        self.lblStars = QtWidgets.QLabel(self.widgetDesc)
        self.lblStars.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblStars.setObjectName("lblStars")
        self.gridLayout_7.addWidget(self.lblStars, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widgetDesc)
        self.label_9.setMinimumSize(QtCore.QSize(0, 28))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 4, 0, 1, 1)
        self.lblCover = QtWidgets.QLabel(self.widgetTop_2)
        self.lblCover.setGeometry(QtCore.QRect(40, 20, 190, 260))
        self.lblCover.setMinimumSize(QtCore.QSize(190, 260))
        self.lblCover.setMaximumSize(QtCore.QSize(190, 260))
        self.lblCover.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lblCover.setText("")
        self.lblCover.setObjectName("lblCover")
        self.gridLayout_5.addWidget(self.widgetTop_2, 0, 0, 1, 1)
        self.widgetBottom = QtWidgets.QWidget(self.pageDetail)
        self.widgetBottom.setStyleSheet("")
        self.widgetBottom.setObjectName("widgetBottom")
        self.grid000 = QtWidgets.QGridLayout(self.widgetBottom)
        self.grid000.setContentsMargins(15, 5, 15, 20)
        self.grid000.setObjectName("grid000")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widgetBottom)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollBtns = QtWidgets.QWidget()
        self.scrollBtns.setGeometry(QtCore.QRect(0, 0, 70, 18))
        self.scrollBtns.setObjectName("scrollBtns")
        self.gridBtns = QtWidgets.QGridLayout(self.scrollBtns)
        self.gridBtns.setContentsMargins(9, 9, -1, -1)
        self.gridBtns.setObjectName("gridBtns")
        self.scrollArea_2.setWidget(self.scrollBtns)
        self.grid000.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widgetBottom, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageDetail)
        self.pageNoResult = QtWidgets.QWidget()
        self.pageNoResult.setObjectName("pageNoResult")
        self.label_2 = QtWidgets.QLabel(self.pageNoResult)
        self.label_2.setGeometry(QtCore.QRect(340, 170, 291, 151))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.pageNoResult)
        self.gridMain.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.widgetTools = QtWidgets.QWidget(mainForm)
        self.widgetTools.setMinimumSize(QtCore.QSize(0, 34))
        self.widgetTools.setMaximumSize(QtCore.QSize(16777215, 34))
        self.widgetTools.setStyleSheet("background-color: #2e2e36;")
        self.widgetTools.setObjectName("widgetTools")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widgetTools)
        self.gridLayout_3.setContentsMargins(2, 0, 2, 0)
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblSpace01 = QtWidgets.QLabel(self.widgetTools)
        self.lblSpace01.setText("")
        self.lblSpace01.setObjectName("lblSpace01")
        self.gridLayout_3.addWidget(self.lblSpace01, 0, 10, 1, 1)
        self.lblLastPlay = QtWidgets.QLabel(self.widgetTools)
        self.lblLastPlay.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblLastPlay.setObjectName("lblLastPlay")
        self.gridLayout_3.addWidget(self.lblLastPlay, 0, 8, 1, 1)
        self.btnOpenSource = QtWidgets.QPushButton(self.widgetTools)
        self.btnOpenSource.setMinimumSize(QtCore.QSize(75, 30))
        self.btnOpenSource.setMaximumSize(QtCore.QSize(75, 30))
        self.btnOpenSource.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}")
        self.btnOpenSource.setObjectName("btnOpenSource")
        self.gridLayout_3.addWidget(self.btnOpenSource, 0, 2, 1, 1)
        self.btnBatchDownload = QtWidgets.QPushButton(self.widgetTools)
        self.btnBatchDownload.setMinimumSize(QtCore.QSize(75, 30))
        self.btnBatchDownload.setMaximumSize(QtCore.QSize(75, 30))
        self.btnBatchDownload.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}")
        self.btnBatchDownload.setObjectName("btnBatchDownload")
        self.gridLayout_3.addWidget(self.btnBatchDownload, 0, 4, 1, 1)
        self.btnNext = QtWidgets.QPushButton(self.widgetTools)
        self.btnNext.setEnabled(False)
        self.btnNext.setMinimumSize(QtCore.QSize(75, 30))
        self.btnNext.setMaximumSize(QtCore.QSize(75, 30))
        self.btnNext.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: #bababa;\n"
"color: #ffffff;\n"
"}")
        self.btnNext.setObjectName("btnNext")
        self.gridLayout_3.addWidget(self.btnNext, 0, 12, 1, 1)
        self.lblLastPlayEpisodeName = QtWidgets.QLabel(self.widgetTools)
        self.lblLastPlayEpisodeName.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblLastPlayEpisodeName.setObjectName("lblLastPlayEpisodeName")
        self.gridLayout_3.addWidget(self.lblLastPlayEpisodeName, 0, 9, 1, 1)
        self.btnSetting = QtWidgets.QPushButton(self.widgetTools)
        self.btnSetting.setMinimumSize(QtCore.QSize(75, 30))
        self.btnSetting.setMaximumSize(QtCore.QSize(75, 30))
        self.btnSetting.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}")
        self.btnSetting.setObjectName("btnSetting")
        self.gridLayout_3.addWidget(self.btnSetting, 0, 3, 1, 1)
        self.btnGetAllLinks = QtWidgets.QPushButton(self.widgetTools)
        self.btnGetAllLinks.setEnabled(False)
        self.btnGetAllLinks.setMinimumSize(QtCore.QSize(75, 30))
        self.btnGetAllLinks.setMaximumSize(QtCore.QSize(75, 30))
        self.btnGetAllLinks.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: #bababa;\n"
"color: #ffffff;\n"
"}")
        self.btnGetAllLinks.setObjectName("btnGetAllLinks")
        self.gridLayout_3.addWidget(self.btnGetAllLinks, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(828, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 7, 1, 1)
        self.lblLastPlayEpisodeNum = QtWidgets.QLabel(self.widgetTools)
        self.lblLastPlayEpisodeNum.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblLastPlayEpisodeNum.setObjectName("lblLastPlayEpisodeNum")
        self.gridLayout_3.addWidget(self.lblLastPlayEpisodeNum, 0, 11, 1, 1)
        self.btnAbout = QtWidgets.QPushButton(self.widgetTools)
        self.btnAbout.setMinimumSize(QtCore.QSize(75, 30))
        self.btnAbout.setMaximumSize(QtCore.QSize(75, 30))
        self.btnAbout.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}")
        self.btnAbout.setObjectName("btnAbout")
        self.gridLayout_3.addWidget(self.btnAbout, 0, 1, 1, 1)
        self.btnUpdataLogs = QtWidgets.QPushButton(self.widgetTools)
        self.btnUpdataLogs.setMinimumSize(QtCore.QSize(75, 30))
        self.btnUpdataLogs.setMaximumSize(QtCore.QSize(75, 30))
        self.btnUpdataLogs.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}")
        self.btnUpdataLogs.setObjectName("btnUpdataLogs")
        self.gridLayout_3.addWidget(self.btnUpdataLogs, 0, 6, 1, 1)
        self.btnHowToUse = QtWidgets.QPushButton(self.widgetTools)
        self.btnHowToUse.setMinimumSize(QtCore.QSize(75, 30))
        self.btnHowToUse.setMaximumSize(QtCore.QSize(75, 30))
        self.btnHowToUse.setStyleSheet("QPushButton{\n"
"background-color: #2e2e36;\n"
"color: #bababa;\n"
"font: 10pt \"微软雅黑\";\n"
"border: 1px solid #bababa;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #000000;\n"
"color: #ffffff;\n"
"}")
        self.btnHowToUse.setObjectName("btnHowToUse")
        self.gridLayout_3.addWidget(self.btnHowToUse, 0, 5, 1, 1)
        self.gridMain.addWidget(self.widgetTools, 2, 0, 1, 1)
        self.widgetTop = QtWidgets.QWidget(mainForm)
        self.widgetTop.setMinimumSize(QtCore.QSize(0, 55))
        self.widgetTop.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widgetTop.setStyleSheet("\n"
"\n"
"background-color: #292931;\n"
"\n"
"/*\n"
"background-color: rgb(255, 255, 255)\n"
"background-color: #303038;\n"
"*/")
        self.widgetTop.setObjectName("widgetTop")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widgetTop)
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.btnBack = QtWidgets.QPushButton(self.widgetTop)
        self.btnBack.setMinimumSize(QtCore.QSize(30, 30))
        self.btnBack.setMaximumSize(QtCore.QSize(30, 30))
        self.btnBack.setStyleSheet("background-color: #ffffff;\n"
"border-radius:0;\n"
"")
        self.btnBack.setText("")
        self.btnBack.setObjectName("btnBack")
        self.gridLayout_9.addWidget(self.btnBack, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 1, 1, 1)
        self.widgetSearch = QtWidgets.QWidget(self.widgetTop)
        self.widgetSearch.setMinimumSize(QtCore.QSize(400, 45))
        self.widgetSearch.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widgetSearch.setStyleSheet("")
        self.widgetSearch.setObjectName("widgetSearch")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widgetSearch)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.btnSearch = QtWidgets.QPushButton(self.widgetSearch)
        self.btnSearch.setMinimumSize(QtCore.QSize(80, 38))
        self.btnSearch.setMaximumSize(QtCore.QSize(80, 38))
        self.btnSearch.setStyleSheet("QPushButton{\n"
"background-color: #44444f;\n"
"color: #ff5246;\n"
"border-top-right-radius : 19px;\n"
"border-bottom-right-radius : 19px;\n"
"border-top-left-radius : 0;\n"
"font: 12pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff5246;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"color: #7f7f7f;\n"
"}")
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout_8.addWidget(self.btnSearch, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.widgetSearch)
        self.widget.setStyleSheet("background-color: #393942;\n"
"border-radius : 0;")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(252, 38))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 38))
        self.widget_2.setStyleSheet("background:transent;\n"
"\n"
"background-color: #292931;")
        self.widget_2.setObjectName("widget_2")
        self.gridSearchBar = QtWidgets.QGridLayout(self.widget_2)
        self.gridSearchBar.setContentsMargins(0, 0, 0, 0)
        self.gridSearchBar.setSpacing(0)
        self.gridSearchBar.setObjectName("gridSearchBar")
        self.horizontalLayout.addWidget(self.widget_2)
        self.comboSelectInterface = QtWidgets.QComboBox(self.widget)
        self.comboSelectInterface.setMinimumSize(QtCore.QSize(68, 38))
        self.comboSelectInterface.setMaximumSize(QtCore.QSize(68, 38))
        self.comboSelectInterface.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboSelectInterface.setStyleSheet("QComboBox {\n"
"color: #bababa;\n"
"background:transparent;\n"
"font: 12pt \"微软雅黑\";\n"
"border-radius : 0;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"outline: 0px solid gray;\n"
"border: 1px solid #393942;\n"
"color: #bababa;\n"
"background-color: #393942;\n"
"selection-background-color: #7f7f7f;\n"
"}")
        self.comboSelectInterface.setObjectName("comboSelectInterface")
        self.comboSelectInterface.addItem("")
        self.comboSelectInterface.addItem("")
        self.horizontalLayout.addWidget(self.comboSelectInterface)
        self.gridLayout_8.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.widgetSearch, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 0, 3, 1, 1)
        self.widgetCrrlBtns = QtWidgets.QWidget(self.widgetTop)
        self.widgetCrrlBtns.setMinimumSize(QtCore.QSize(111, 0))
        self.widgetCrrlBtns.setStyleSheet("/*\n"
"border: 1px solid #393942;\n"
"*/")
        self.widgetCrrlBtns.setObjectName("widgetCrrlBtns")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widgetCrrlBtns)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.btnMinSize = QtWidgets.QPushButton(self.widgetCrrlBtns)
        self.btnMinSize.setMinimumSize(QtCore.QSize(16, 16))
        self.btnMinSize.setMaximumSize(QtCore.QSize(16, 16))
        self.btnMinSize.setStyleSheet("border-radius:0;")
        self.btnMinSize.setText("")
        self.btnMinSize.setObjectName("btnMinSize")
        self.gridLayout_10.addWidget(self.btnMinSize, 0, 0, 1, 1)
        self.btnMaxSize = QtWidgets.QPushButton(self.widgetCrrlBtns)
        self.btnMaxSize.setMinimumSize(QtCore.QSize(16, 16))
        self.btnMaxSize.setMaximumSize(QtCore.QSize(16, 16))
        self.btnMaxSize.setStyleSheet("border-radius:0;")
        self.btnMaxSize.setText("")
        self.btnMaxSize.setObjectName("btnMaxSize")
        self.gridLayout_10.addWidget(self.btnMaxSize, 0, 1, 1, 1)
        self.btnClose = QtWidgets.QPushButton(self.widgetCrrlBtns)
        self.btnClose.setMinimumSize(QtCore.QSize(16, 16))
        self.btnClose.setMaximumSize(QtCore.QSize(16, 16))
        self.btnClose.setStyleSheet("border-radius:0;")
        self.btnClose.setText("")
        self.btnClose.setObjectName("btnClose")
        self.gridLayout_10.addWidget(self.btnClose, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.widgetCrrlBtns, 0, 4, 1, 1)
        self.gridMain.addWidget(self.widgetTop, 0, 0, 1, 1)

        self.retranslateUi(mainForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "看番神器"))
        self.lblTitle.setText(_translate("mainForm", "标题"))
        self.lblArea.setText(_translate("mainForm", "地区"))
        self.lblTime.setText(_translate("mainForm", "年代"))
        self.label_5.setText(_translate("mainForm", "地区："))
        self.label_6.setText(_translate("mainForm", "类型："))
        self.label_7.setText(_translate("mainForm", "年代："))
        self.lblType.setText(_translate("mainForm", "类型"))
        self.lblStars.setText(_translate("mainForm", "演员："))
        self.label_9.setText(_translate("mainForm", "演员："))
        self.label_2.setText(_translate("mainForm", "啥都没有"))
        self.lblLastPlay.setText(_translate("mainForm", "最近一次播放："))
        self.btnOpenSource.setText(_translate("mainForm", "项目地址"))
        self.btnBatchDownload.setText(_translate("mainForm", "批量下载"))
        self.btnNext.setText(_translate("mainForm", "下一集"))
        self.lblLastPlayEpisodeName.setText(_translate("mainForm", "无"))
        self.btnSetting.setText(_translate("mainForm", "设置"))
        self.btnGetAllLinks.setText(_translate("mainForm", "抓取链接"))
        self.lblLastPlayEpisodeNum.setText(_translate("mainForm", "第0集"))
        self.btnAbout.setText(_translate("mainForm", "关于"))
        self.btnUpdataLogs.setText(_translate("mainForm", "更新日志"))
        self.btnHowToUse.setText(_translate("mainForm", "使用教程"))
        self.btnBack.setToolTip(_translate("mainForm", "返回"))
        self.btnSearch.setToolTip(_translate("mainForm", "o(*≧▽≦)ツ"))
        self.btnSearch.setText(_translate("mainForm", "搜索"))
        self.comboSelectInterface.setItemText(0, _translate("mainForm", "接口1"))
        self.comboSelectInterface.setItemText(1, _translate("mainForm", "接口2"))
        self.btnMinSize.setToolTip(_translate("mainForm", "最小化"))
        self.btnMaxSize.setToolTip(_translate("mainForm", "象征性的按钮，意义不大\n"
"最大化了反而会影响观感"))
        self.btnClose.setToolTip(_translate("mainForm", "关闭"))
