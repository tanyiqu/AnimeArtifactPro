import threading
import time
import webbrowser
import json
from functools import partial

from PyQt5 import QtGui, sip
from PyQt5.QtGui import QTextCursor

import R
from Configuration import Configuration
import ui.ui_designer.ui_file.ui_form_mainForm
from Utils import CrawlUtil
from Signals import SearchFinish, DetailFinish
from Utils.WebUtil import setLabelImg
from ui.Widgets.ItemWidget import ItemWidget


class MainForm(ui.ui_designer.ui_file.ui_form_mainForm.Ui_mainForm):
    # 信号
    searchFinish = ''   # 搜索完成
    detailFinish = ''   # 获取详情完成

    # 线程
    # 搜索动漫线程
    thread_search = ''
    # 加载动漫详情
    thread_detail = ''

    config = ''
    searchResult = ''
    detailResult = ''
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
        self.detailFinish = DetailFinish()
        self.thread_search = threading.Thread(target=self._search, name='')
        self.thread_detail = threading.Thread(target=self._detail, name='')
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
        # 获取详情完成
        self.detailFinish.signal.connect(self._detailFinish)
        # 关于
        self.btnAbout.clicked.connect(lambda: print('关于'))
        # 项目地址
        self.btnOpenSource.clicked.connect(lambda: webbrowser.open_new(R.string.OPEN_SOURCE))
        # 返回
        self.btnBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        pass

    # 点击搜索按钮
    def search(self):
        if self.thread_search.is_alive():
            self.log('正在搜索中！请稍后再试！')
            return
        if self.thread_detail.is_alive():
            self.log('正在获取详情中！请稍后再试！')
            return
        # 清除现有的搜索结果
        while self.grid.count() != 0:
            w = self.grid.itemAt(0).widget()
            self.grid.removeWidget(w)
            sip.delete(w)
        # 获取输入的关键词
        self.searchword = self.txtSearchword.text().strip()
        # if self.searchword == R.string.NONE:
        #     self.log('【警告】请输入关键词！')
        #     return
        self.stackedWidget.setCurrentIndex(1)
        print('搜索：', self.searchword)
        self.log('正在搜索：「' + self.searchword + '」')
        self.log('...')
        # 根据输入获取json数组
        # 开启线程搜索
        # 因为线程只能被执行一次，所以只要线程没有在运行就得生成新的线程
        self.thread_search = threading.Thread(target=self._search, name='')
        self.thread_search.start()
        pass

    # 搜索 线程执行
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

        # 搜索完成后执行的操作

    # 搜索完成时执行
    def _searchFinished(self):
        self.log('「' + self.searchword + '」搜索完成！共{}项结果.'.format(len(self.searchResult)))
        # 如果没有搜到任何结果就跳到没有结果页
        if len(self.searchResult) == 0:
            self.stackedWidget.setCurrentIndex(3)
            return
        print('搜索完成')
        r = 0
        c = 0
        for result in self.searchResult:
            w = ItemWidget(result['url'], result['title'], result['cover'], result['latest'])
            # 点击事件
            d = {
                'url': result['url'],
                'cover': result['cover'],
                'title': result['title']
            }
            w.itemWidgetMouseRelease.signal.connect(partial(self.detail, d))
            self.grid.addWidget(w, r, c)
            c += 1
            if c == 4:
                c = 0
                r += 1
            pass
        pass

    def detail(self, params):
        """
        跳转到详情页
        :param params: 参数字典
        :return: None
        """
        # 跳转到详情页
        self.stackedWidget.setCurrentIndex(2)
        print(params['url'])
        self.log_secondary('正在访问「' + params['title'] + '」')
        self.log_secondary('正在获取详情信息')
        self.log_secondary('...')
        self.lblTitle.setText(params['title'])
        # 因为已经拿到封面了，可以在这里加载封面
        t = threading.Thread(target=setLabelImg, name='', args=(self.lblCover, params['cover'],))
        t.start()
        self.thread_detail = threading.Thread(target=self._detail, name='')
        self.thread_detail.start()
        pass

    def _detail(self):
        print('执行')

        # 发射获取完成的信号
        self.detailFinish.signal.emit()
        pass

    def _detailFinish(self):
        self.log_secondary('获取完成！')
        # 在这里加载详情信息
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
