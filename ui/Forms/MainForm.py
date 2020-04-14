from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
# noinspection PyProtectedMember
from ui.Forms._Forms._MainForm import _MainForm
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import R


class MainForm(QWidget):
    """
    主窗口类
    对窗口的操作放在此类
    """
    _startPos = None
    _endPos = None
    _isTracking = False

    _isMaxing = False
    # 最大化之前的大小
    lastSize = None

    def __init__(self):
        super().__init__()
        self.mainForm = _MainForm()
        self.mainForm.setupUi(self)
        self.mainForm.init()
        # 初始化外观
        self.initAppearance()
        # 功能操作（关闭窗口等）
        self.initFunc()
        pass

    def initAppearance(self):
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 标题
        self.setWindowTitle(R.string.APP_NAME)
        # 图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # 加载欢迎图片
        # self.mainForm.lblWelcomeImg.setFixedSize(800,400)
        # url = 'https://cn.bing.com//th?id=OHR.WatChaloem_ZH-CN8722271527_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'
        # setLabelImg(self.mainForm.lblWelcomeImg, url)
        pass

    def initFunc(self):
        # 关闭窗口
        self.mainForm.btnClose.clicked.connect(self.close)
        # 最小化
        self.mainForm.btnMinSize.clicked.connect(self.showMinimized)
        # 最大化
        self.mainForm.btnMaxSize.clicked.connect(self._maxSize)
        pass

    def _maxSize(self):
        if self._isMaxing:
            self.resize(self.lastSize)
            self._isMaxing = False
        else:
            self.lastSize = self.size()
            self.showMaximized()
            self._isMaxing = True
        pass

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        # if e.button() == Qt.LeftButton and self.inMovingArea(e.pos()):
        if self._isTracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    # 鼠标按下
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton and self.inMovingArea(e.pos()):
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton and self.inMovingArea(e.pos()):
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    # 判断该点是否在可拖动的区域
    def inMovingArea(self, pos: QPoint):
        if 0 <= pos.y() <= 55:
            return True
        return False

    pass
