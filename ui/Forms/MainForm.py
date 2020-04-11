import threading
import time
import webbrowser
import json

from PyQt5 import QtGui
from PyQt5.QtGui import QTextCursor

import R
import ui.ui_designer.ui_MainForm
from Utils import CrawlUtil, TextUtil


class MainForm(ui.ui_designer.ui_MainForm.Ui_mainForm):

    searchResult = ''
    searchword = ''
    # 线程
    # 搜索动漫线程
    thread_search = ''
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
        # 关于
        self.btnAbout.clicked.connect(lambda: print('关于'))
        # 项目地址
        self.btnOpenSource.clicked.connect(lambda: webbrowser.open_new(R.string.OPEN_SOURCE))
        pass

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

    def _search(self):
        # 获取搜索的数据
        self.searchResult = CrawlUtil.search(self.searchword, self.interface)
        # 发射搜索完成的信号
        # 将json格式化成python内置的列表对象
        self.searchResult = json.loads(self.searchResult)
        # 解析成app标准的列表
        self.searchResult = CrawlUtil.parseSearchResult(self.searchResult, self.interface)
        print(self.searchResult)
        self.log('「' + self.searchword + '」搜索完成！共{}项结果.'.format(len(self.searchResult)))
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
