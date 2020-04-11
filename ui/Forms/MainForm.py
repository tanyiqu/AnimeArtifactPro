import threading
import time
import webbrowser
import json

from PyQt5 import QtGui
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QWidget

import R
from Configuration import Configuration
import ui.ui_designer.ui_file.ui_form_mainForm
from Utils import CrawlUtil
from Signals import SearchFinish
from ui.Widgets.Item import Item


class MainForm(ui.ui_designer.ui_file.ui_form_mainForm.Ui_mainForm):
    # 信号
    searchFinish = ''  # 搜索完成

    # 线程
    # 搜索动漫线程
    thread_search = ''

    config = ''
    searchResult = ''
    searchword = ''
    interface = 1

    def init(self, mainForm):
        # 标题
        mainForm.setWindowTitle(R.string.APP_NAME)
        # 图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        # 初始化变量
        self.initVars()
        # 欢迎
        self.welcome()
        # 连接信号槽
        self.do_connect()
        pass

    def initVars(self):
        """
        初始化变量
        :return: None
        """
        self.config = Configuration.getInstance()
        self.searchFinish = SearchFinish()
        self.thread_search = threading.Thread(target=self._search, name='')
        pass

    def welcome(self):
        self.log(R.string.WELCOME)
        pass

    def do_connect(self):
        """
        连接信号槽
        :return:
        """
        # 搜索
        self.btnSearch.clicked.connect(self.search)
        # 搜索完成
        self.searchFinish.signal.connect(self._searchFinished)
        # 关于
        self.btnAbout.clicked.connect(lambda: print('关于'))
        # 项目地址
        self.btnOpenSource.clicked.connect(lambda: webbrowser.open_new(R.string.OPEN_SOURCE))

        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        pass

    # 搜索完成后执行的操作
    def _searchFinished(self):
        self.log('「' + self.searchword + '」搜索完成！共{}项结果.'.format(len(self.searchResult)))
        print('搜索完成')
        for result in self.searchResult:
            w = QWidget()
            i = Item(result['title'], '', '')
            i.setupUi(w)
            i.init()
            self.layout_scroll.addChildWidget(w)
            pass
        pass

    # 点击搜索按钮
    def search(self):
        if self.thread_search.is_alive():
            self.log('正在搜索中！请稍后再试！')
            return
        # 获取输入的关键词
        self.searchword = self.txtSearchword.text().strip()
        if self.searchword == R.string.NONE:
            self.log('【警告】请输入关键词！')
            return
        print('搜索：', self.searchword)
        self.log('正在搜索：「' + self.searchword + '」')
        self.log('...')
        # 根据输入获取json数组
        # 开启线程搜索
        # 因为线程只能被执行一次，所以只要线程没有在运行就得生成新的线程
        self.thread_search = threading.Thread(target=self._search, name='')
        self.thread_search.start()
        pass

    # 搜索
    def _search(self):
        # 获取搜索的数据
        self.searchResult = CrawlUtil.search(self.searchword, self.interface)
        # 将json格式化成python内置的列表对象
        self.searchResult = json.loads(self.searchResult)
        # 解析成app标准的列表
        self.searchResult = CrawlUtil.parseSearchResult(self.searchResult, self.interface)
        print(self.searchResult)
        # 发射搜索完成的信号
        self.searchFinish.signal.emit()
        pass

    def log(self, msg, showTime=True):
        if showTime:
            t = time.strftime('%H:%M:%S', time.localtime())
            msg = t + ' ' + msg.strip()
        self.console1.appendPlainText(msg)
        cursor = self.console1.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console1.setTextCursor(cursor)
        pass

    def log_secondary(self, msg, showTime=True):
        msg = msg.strip()
        if showTime:
            t = time.strftime('%H:%M:%S', time.localtime())
            msg = t + ' ' + msg
        self.console2.appendPlainText(msg)
        cursor = self.console2.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console2.setTextCursor(cursor)
        pass

    pass
