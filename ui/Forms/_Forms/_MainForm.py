import re
import threading
import time
import json
from functools import partial

import requests
from PyQt5 import sip
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QTextCursor

import R
from Configuration import Configuration
import ui.ui_designer.ui_file.uic_mainForm
from Utils import VideoUtil
from Signals import SearchFinish, DetailFinish, UpdateSignal
from Utils.CrawlInterfaces.CrawlImpl_01 import CrawlImpl_01
from Utils.CrawlInterfaces.CrawlImpl_02 import CrawlImpl_02
from Utils.CrawlInterfaces.CrawlImpl_03 import CrawlImpl_03
from Utils.CrawlInterfaces.CrawlImpl_04 import CrawlImpl_04
from Utils.CrawlInterfaces.CrawlImpl_05 import CrawlImpl_05
from Utils.WebUtil import setLabelImg
from ui.Widgets.ItemWidget import ItemWidget
from ui.Widgets.SearchBarWidget import SearchBarWidget
from ui.Widgets.WelcomeWidget import WelcomeWidget

# noinspection PyProtectedMember
from ui.Widgets._Widgets.EpisodeButton import EpisodeButton


class _MainForm(ui.ui_designer.ui_file.uic_mainForm.Ui_mainForm):
    """
    继承pyuic生成的类
    在此类中做逻辑操作
    主要是调用爬虫等操作
    """

    # 核心变量
    config = None  # 全局配置
    crawlImpl = None  # 接口实现类

    # 信号
    searchFinish = None  # 搜索完成
    detailFinish = None  # 获取详情完成
    updateSignal = None

    # 线程
    thread_search = None  # 搜索动漫线程
    thread_detail = None  # 加载动漫详情
    thread_getAllLinks = None  # 抓取所有链接
    thread_getUpdates = None  # 获取更新信息

    # 字符串变量
    searchword = ''  # 关键词
    currentEName = ''  # 当前番剧的名字
    currentEUrl = ''  # 当前番剧的链接

    # 控件
    welcomeWidget = None  # 欢迎面板
    txtSearchword = None  # 搜索输入框

    #
    searchResult = None  # 存放搜索的结果
    detailResult = None  # 存放动漫的详情信息 如：{1: ['第1集'.'第1集的url'], 2: ['第2集'.'第2集的url']}

    def init(self):
        # 加上搜索输入框
        self.txtSearchword = SearchBarWidget()
        self.gridSearchBar.addWidget(self.txtSearchword, 0, 0)
        # 初始化变量
        self.initVars()
        # 欢迎
        self.welcome()
        # 连接信号槽
        self.do_connect()
        # 其他
        self.func()
        pass

    def initVars(self):
        """
        初始化变量
        :return: None
        """
        self.config = Configuration()
        # 根据配置文件选择接口
        # if self.config.curr_interface == 1:
        #     self.crawlImpl = CrawlImpl_01()
        self.crawlImpl = CrawlImpl_01()
        self.welcomeWidget = WelcomeWidget()
        self.gridWelcome.addWidget(self.welcomeWidget, 0, 0)
        self.searchFinish = SearchFinish()
        self.detailFinish = DetailFinish()
        self.updateSignal = UpdateSignal()
        self.thread_search = threading.Thread(target=self._search, name='')
        self.thread_detail = threading.Thread(target=self._detail, name='')
        self.thread_getAllLinks = threading.Thread(target=self.crawlImpl.getAllLinks, name='getLinks',
                                                   args=(self.detailResult, self.log_secondary,))
        self.thread_getUpdates = threading.Thread(target=self._checkUpdate, name='checkUpdate')

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
        # 页面切换
        # self.stackedWidget.currentChanged.connect(lambda: self.btnGetAllLinks.setEnabled(False))
        self.stackedWidget.currentChanged.connect(self.pageChanged)
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
        # 下一集
        self.btnNext.clicked.connect(self.playNext)
        # 切换接口
        self.comboSelectInterface.currentIndexChanged.connect(self.changeInterface)
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
        try:
            # 获取搜索的数据
            self.searchResult = self.crawlImpl.search(self.searchword)
            # print(type(self.searchResult), self.searchResult)
            # 将json格式化成python内置的列表对象
            self.searchResult = json.loads(self.searchResult)
            # print('标准化前：', self.searchResult)
            # 解析成app标准的列表
            self.searchResult = self.crawlImpl.parseSearchResult(self.searchResult)
            print('标准化后：', self.searchResult)
            # 发射搜索完成的信号
            self.searchFinish.signal.emit()
            pass
        except Exception as e:
            print('异常', e)
            self.log('请求有点频繁！不知道这个网站怎么搞的！')
            return
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
        self.detailResult = self.crawlImpl.detail(self.log_secondary, url)
        print('detailResult', self.detailResult)
        # 发射获取完成的信号
        self.detailFinish.signal.emit()
        pass

    # 获取详情完成
    def _detailFinish(self):
        if len(self.detailResult) == 0:
            return
        self.log_secondary('番剧获取完毕!')
        self.log_secondary('「' + self.currentEName + '」 总集数：' + str(len(self.detailResult)))
        # 在这里加载详情信息
        r = 0
        c = 0
        # 动态生成对应的按钮
        for i in range(1, len(self.detailResult) + 1):
            result = self.detailResult[i]
            w = EpisodeButton(result[0])
            # w = QPushButton(result[0])
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
        if self.thread_getAllLinks.is_alive():
            self.log('正在抓取链接中！请稍后再试！')
            return
        self.thread_getAllLinks = threading.Thread(target=self.crawlImpl.getAllLinks, name='getLinks',
                                                   args=(self.detailResult, self.log_secondary,))
        self.thread_getAllLinks.start()
        pass

    def playNext(self):
        print('下一集')
        # 找到下一集的播放链接
        old = self.lblLastPlayEpisodeNum.text()
        length = len(self.detailResult)
        n = 1
        for i in range(1, length + 1):
            s = self.detailResult[i]
            if s[0] == old:
                n = i + 1
                break
            pass
        # 找到下一集的编号
        # 如果下一集越界
        if n > length:
            n -= 1
        self.play(self.detailResult[n][0], self.detailResult[n][1])
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
        self.lblLastPlayEpisodeName.setText(self.currentEName)
        self.lblLastPlayEpisodeNum.setText(name)
        self.btnNext.setEnabled(True)

        self.log_secondary('正在播放：' + name)
        # 开启线程获取真实播放链接
        url = self.crawlImpl.getVideoUrl(url)
        # if url[-5:].lower() == '.html':
        #     self.log_secondary('非常抱歉！可能此接口不适合这部番剧><')
        #     self.log_secondary('可以尝试在抓取里的链接播放，或着切换搜索接口！')
        #     return
        self.log_secondary('真实视频播放链接：' + url)
        # # 判断一下能不能用potplayer播放
        # if url[-5:].lower() == '.m3u8':
        #     self.log_secondary('m3u8链接暂时只能用网页解析！')
        VideoUtil.play(url)
        pass

    # 检查更新
    def _checkUpdate(self):
        print('检查更新')
        # 获取当前版本
        currVersion = R.string.UPDATE_LOG[0]['version']
        # 获取新版本
        txt = requests.get('https://tanyiqu.github.io/AnimeArtifactPro/').content.decode('utf-8')
        newVersion = re.findall(r'h3 id=".*?">(.*?)</h3>', txt)[0]
        # 版本匹配
        print('currVersion', currVersion)
        print('newVersion', newVersion)
        if currVersion.strip() == newVersion.strip():
            return
        # 发射更新的信号，让主窗口去处理更新操作
        self.updateSignal.signal.emit()
        pass

    def func(self):
        # 检查更新
        if self.config.checkUpdate:
            QTimer.singleShot(2000, lambda: self.thread_getUpdates.start())
            pass
        # 选择默认接口
        self.comboSelectInterface.setCurrentIndex(self.config.curr_interface - 1)
        pass

    # 页面切换
    def pageChanged(self):
        # 抓取链接禁用
        self.btnGetAllLinks.setEnabled(False)
        # 下一集禁用
        self.btnNext.setEnabled(False)
        # 上次播放清除
        self.lblLastPlayEpisodeNum.setText('第0集')
        self.lblLastPlayEpisodeName.setText('无')
        pass

    def changeInterface(self):
        i = self.comboSelectInterface.currentIndex() + 1
        if i == 1:
            self.crawlImpl = CrawlImpl_01()
            pass
        elif i == 2:
            self.crawlImpl = CrawlImpl_02()
            pass
        elif i == 3:
            self.crawlImpl = CrawlImpl_03()
            pass
        elif i == 4:
            self.crawlImpl = CrawlImpl_04()
            pass
        elif i == 5:
            self.crawlImpl = CrawlImpl_05()
            pass
        else:
            self.crawlImpl = CrawlImpl_01()
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
            self.stackedWidget.setCurrentIndex(index - 1)
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
