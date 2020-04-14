import threading
import time
import json
from functools import partial

from PyQt5 import sip
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QPushButton

import R
from Configuration import Configuration
import ui.ui_designer.ui_file.uic_mainForm
from Utils import CrawlUtil, VideoUtil
from Signals import SearchFinish, DetailFinish
from Utils.WebUtil import setLabelImg
from ui.Widgets.ItemWidget import ItemWidget
from ui.Widgets.WelcomeWidget import WelcomeWidget


class _MainForm(ui.ui_designer.ui_file.uic_mainForm.Ui_mainForm):
    """
    继承pyuic生成的类
    在此类中做逻辑操作
    """

    # 信号
    searchFinish = ''  # 搜索完成
    detailFinish = ''  # 获取详情完成

    # 线程
    # 搜索动漫线程
    thread_search = ''
    # 加载动漫详情
    thread_detail = ''
    # 抓取所有链接
    thread_getAllLinks = ''

    config = ''
    searchResult = ''
    detailResult = ''
    searchword = ''
    interface = 1
    # 当前番剧的名字
    currentEName = ''
    # 当前番剧的链接
    currentEUrl = ''

    welcomeWidget = ''

    def init(self):
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
        self.welcomeWidget = WelcomeWidget()
        self.gridWelcome.addWidget(self.welcomeWidget, 0, 0)
        self.searchFinish = SearchFinish()
        self.detailFinish = DetailFinish()
        self.thread_search = threading.Thread(target=self._search, name='')
        self.thread_detail = threading.Thread(target=self._detail, name='')
        pass

    def welcome(self):
        self.log(R.string.WELCOME)
        self.log_secondary('请搜索！')
        pass

    def do_connect(self):
        """
        连接信号槽
        :return:
        """
        # 页面切换 --> 禁用抓取链接按钮
        self.stackedWidget.currentChanged.connect(lambda: self.btnGetAllLinks.setEnabled(False))
        # 搜索
        self.btnSearch.clicked.connect(self.search)
        # 搜索完成
        self.searchFinish.signal.connect(self._searchFinished)
        # 获取详情完成
        self.detailFinish.signal.connect(self._detailFinish)
        # 返回
        self.btnBack.clicked.connect(self.back)
        # 抓取链接
        self.btnGetAllLinks.clicked.connect(self.getAllLinks)
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
        # print(self.searchResult)
        # 将json格式化成python内置的列表对象
        self.searchResult = json.loads(self.searchResult)
        # print('标准化前：', self.searchResult)
        # 解析成app标准的列表
        self.searchResult = CrawlUtil.parseSearchResult(self.searchResult, self.interface)
        # print('标准化后：', self.searchResult)
        # 发射搜索完成的信号
        self.searchFinish.signal.emit()
        pass

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
            w = ItemWidget(result)
            # 点击事件
            w.itemWidgetMouseRelease.signal.connect(partial(self.detail, result))
            self.grid.addWidget(w, r, c)
            c += 1
            if c == 4:
                c = 0
                r += 1
            pass
        pass

    # 获取详情
    def detail(self, params):
        """
        跳转到详情页
        :param params: 参数字典
        {url', 'cover',  'title', 'latest', 'area', 'time','stars'}
        :return: None
        """
        # 点击了某一部动漫
        print('点击了：' + params['title'])
        self.currentEName = params['title']
        self.currentEUrl = params['url']
        # 跳转到详情页
        self.stackedWidget.setCurrentIndex(2)
        # 在此页面清除原来的搜索结果，方便体验
        while self.gridBtns.count() != 0:
            w = self.gridBtns.itemAt(0).widget()
            self.gridBtns.removeWidget(w)
            sip.delete(w)
        # print(params['url'])
        self.log_secondary('正在访问「' + params['title'] + '」')
        self.log_secondary('正在获取详情信息')
        self.log_secondary('...')

        # print('params：', params)
        # 设置
        notnow = '暂无'
        # 标题
        if params['title'].strip() == R.string.NONE:
            self.lblTitle.setText(notnow)
            pass
        else:
            self.lblTitle.setText(params['title'])
        # 时间
        if params['time'].strip() == R.string.NONE:
            self.lblTime.setText(notnow)
            pass
        else:
            self.lblTime.setText(params['time'])
        # 地区
        if params['area'].strip() == R.string.NONE:
            self.lblArea.setText(notnow)
            pass
        else:
            self.lblArea.setText(params['area'])
        # 演员
        if params['stars'].strip() == R.string.NONE:
            self.lblStars.setText(notnow)
            pass
        else:
            self.lblStars.setText(params['stars'])
        # 加载封面
        t = threading.Thread(target=setLabelImg, name='', args=(self.lblCover, params['cover'],))
        t.start()
        self.thread_detail = threading.Thread(target=self._detail, name='', args=(params['url'],))
        self.thread_detail.start()
        pass

    # 获取详情 线程执行
    def _detail(self, url):
        print('执行')
        self.detailResult = CrawlUtil.detail(url, self.log_secondary, self.interface)
        print(self.detailResult)
        # 发射获取完成的信号
        self.detailFinish.signal.emit()
        pass

    # 获取详情完成
    def _detailFinish(self):
        self.log_secondary('番剧获取完毕!')
        self.log_secondary('「' + self.currentEName + '」 总集数：' + str(len(self.detailResult)))
        # 在这里加载详情信息
        r = 0
        c = 0
        # 动态生成对应的按钮
        for i in range(1, len(self.detailResult) + 1):
            result = self.detailResult[i]
            w = QPushButton(result[0])
            w.clicked.connect(partial(self.play, result[0], result[1]))
            w.setFixedSize(120, 35)
            self.gridBtns.addWidget(w, r, c)
            c += 1
            if c == 7:
                c = 0
                r += 1
            i += 1
            pass
        self.btnGetAllLinks.setEnabled(True)
        pass

    # 抓取链接
    def getAllLinks(self):
        t = threading.Thread(target=CrawlUtil.getAllLinks, name='getLinks', args=(self.detailResult, self.log_secondary, self.interface,))
        t.start()
        pass

    # 播放
    def play(self, name, url):
        """
        播放
        :param name: 第几集
        :param url: 真实url
        :return: None
        """
        print('播放', url)
        self.log_secondary('正在播放：' + name)
        # 开启线程获取真实播放链接
        url = CrawlUtil.getVideoUrl(url, self.interface)
        self.log_secondary('真实视频播放链接：' + url)
        # 判断一下能不能用potplayer播放
        if url[-5:].lower() == '.m3u8':
            self.log_secondary('m3u8链接暂时只能用网页解析！')
        VideoUtil.play(url)
        pass

    # 返回
    def back(self):
        index = self.stackedWidget.currentIndex()
        # 在首页，不操作
        if index == 0:
            pass
        # 在搜索结果为空页,返回首页
        elif index == 3:
            self.stackedWidget.setCurrentIndex(0)
            pass
        # 其余的返回上一页
        else:
            self.stackedWidget.setCurrentIndex(index-1)
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
        msg = str(msg).strip()
        if showTime:
            t = time.strftime('%H:%M:%S', time.localtime())
            msg = t + ' ' + msg
        self.console2.appendPlainText(msg)
        cursor = self.console2.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console2.setTextCursor(cursor)
        pass

    pass
