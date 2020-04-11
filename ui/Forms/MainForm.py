import threading
import time
import webbrowser

from PyQt5 import QtGui
from PyQt5.QtGui import QTextCursor

import R
import ui.ui_designer.ui_MainForm
from Utils import CrawlUtil


class MainForm(ui.ui_designer.ui_MainForm.Ui_mainForm):

    sousuoJson = ''

    def init(self, mainForm):
        # 标题
        mainForm.setWindowTitle(R.string.APP_NAME)
        # 图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        # 欢迎
        self.welcome()
        # 连接信号槽
        self.do_connect()
        pass

    def welcome(self):
        self.log(R.string.WELCOME)
        pass

    def do_connect(self):
        """
        做连接信号槽
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
        # 获取输入的关键词
        searchword = self.searchword.text().strip()
        if searchword == R.string.NONE:
            self.log('【警告】请输入关键词！')
            return
        print('搜索：', searchword)
        self.log('正在搜索：「' + searchword + '」')
        self.log('...')
        # 根据输入获取json数组
        # 开启线程搜索
        t = threading.Thread(target=self._search, name='', args=(searchword,))
        t.start()
        pass

    def _search(self, searchword):
        self.sousuoJson = CrawlUtil.search(searchword)
        print(self.sousuoJson)
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
