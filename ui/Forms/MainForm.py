from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QMouseEvent, QPainter, QPixmap
# noinspection PyProtectedMember
from ui.Forms._Forms._MainForm import _MainForm
from PyQt5.QtWidgets import QWidget


class MainForm(QWidget):
    """
    主窗口类
    对窗口的操作放在此类
    """
    _startPos = None
    _endPos = None
    _isTracking = False

    SHADOW_WIDTH = 8
    pixmaps = []

    _isMaxing = False
    # 最大尺寸
    maxSize = None
    # 最大化之前的大小
    lastSize = None
    # 最大化之前的位置
    lastPos = None

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
        # 设置窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 按钮
        # 关闭
        self.mainForm.btnClose.setStyleSheet("QPushButton{border-image: url(resource/imgs/close_normal.png)}"
                                             "QPushButton:hover{border-image: url(resource/imgs/close_hover.png)}"
                                             "QPushButton:pressed{border-image: url(resource/imgs/close_pressed.png)}")
        # 最小化
        self.mainForm.btnMinSize.setStyleSheet("QPushButton{border-image: url(resource/imgs/min_normal.png)}"
                                               "QPushButton:hover{border-image: url(resource/imgs/min_hover.png)}"
                                               "QPushButton:pressed{border-image: url(resource/imgs/min_pressed.png)}")
        # 最大化
        self.mainForm.btnMaxSize.setStyleSheet("QPushButton{border-image: url(resource/imgs/max_normal.png)}"
                                               "QPushButton:hover{border-image: url(resource/imgs/max_hover.png)}"
                                               "QPushButton:pressed{border-image: url(resource/imgs/max_pressed.png)}")
        # 返回
        self.mainForm.btnBack.setStyleSheet("QPushButton{border-image: url(resource/imgs/back_normal.png)}"
                                            "QPushButton:hover{border-image: url(resource/imgs/back_hover.png)}"
                                            "QPushButton:pressed{border-image: url(resource/imgs/back_pressed.png)}")
        # 加载欢迎图片
        # self.mainForm.lblWelcomeImg.setFixedSize(800,400)
        #         # url = 'https://cn.bing.com//th?id=OHR.WatChaloem_ZH-CN8722271527_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'
        #         # setLabelImg(self.mainForm.lblWelcomeImg, url)
        pass

    def initFunc(self):
        # 关闭窗口
        self.mainForm.btnClose.clicked.connect(self.close)
        # 最小化
        self.mainForm.btnMinSize.clicked.connect(self.showMinimized)
        # 最大化
        self.mainForm.btnMaxSize.clicked.connect(self._maxSize)
        pass

    # 点击最大化
    def _maxSize(self):
        """
        如果当前不是最大化状态，就最大化
        如果是最大化状态就还原
        """
        if not self._isMaxing:
            print('最大化')
            self.lastSize = self.size()
            self.lastPos = self.pos()
            self.mainForm.gridMain.setContentsMargins(0, 0, 0, 0)
            # showMaximized()有时候无响应，所但是第一次基本上都会相应
            # 所以第一次最大化后，记录一下尺寸

            if self.maxSize is None:
                # self.showMaximized()
                # 使用这种方式最大化
                self.setWindowState(Qt.WindowMaximized)
                self.maxSize = self.size()
                pass
            else:
                self.move(0, 0)
                self.resize(self.maxSize)
                pass
            self._isMaxing = True
            pass
        else:
            print('还原')
            self.move(self.lastPos)
            self.resize(self.lastSize)
            self.mainForm.gridMain.setContentsMargins(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                                                      self.SHADOW_WIDTH)
            self._isMaxing = False
            pass
        pass

    def drawShadow(self, painter):
        # 绘制左上角、左下角、右上角、右下角、上、下、左、右边框
        self.pixmaps.append(str("resource/imgs/shadow/left_top.png"))
        self.pixmaps.append(str("resource/imgs/shadow/left_bottom.png"))
        self.pixmaps.append(str("resource/imgs/shadow/right_top.png"))
        self.pixmaps.append(str("resource/imgs/shadow/right_bottom.png"))
        self.pixmaps.append(str("resource/imgs/shadow/top_mid.png"))
        self.pixmaps.append(str("resource/imgs/shadow/bottom_mid.png"))
        self.pixmaps.append(str("resource/imgs/shadow/left_mid.png"))
        self.pixmaps.append(str("resource/imgs/shadow/right_mid.png"))
        painter.drawPixmap(0, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[0]))  # 左上角
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[2]))  # 右上角
        painter.drawPixmap(0, self.height() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[1]))  # 左下角
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH, QPixmap(self.pixmaps[3]))  # 右下角
        painter.drawPixmap(0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[6]).scaled(self.SHADOW_WIDTH,
                                                           self.height() - 2 * self.SHADOW_WIDTH))  # 左
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           self.height() - 2 * self.SHADOW_WIDTH, QPixmap(self.pixmaps[7]).scaled(self.SHADOW_WIDTH,
                                                                                                  self.height() - 2 * self.SHADOW_WIDTH))  # 右
        painter.drawPixmap(self.SHADOW_WIDTH, 0, self.width() - 2 * self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[4]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                           self.SHADOW_WIDTH))  # 上
        painter.drawPixmap(self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH, self.width() - 2 * self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH, QPixmap(self.pixmaps[5]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                                              self.SHADOW_WIDTH))  # 下

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(QRect(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width() - 2 * self.SHADOW_WIDTH,
                               self.height() - 2 * self.SHADOW_WIDTH))

    # 鼠标移动

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

    # 鼠标释放
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
