import threading

from PyQt5.QtCore import QTimer, QDateTime, QPropertyAnimation, QPoint
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget

# noinspection PyProtectedMember
from ui.Widgets._Widgets._WelcomeWidget import _WelcomeWidget


class WelcomeWidget(QWidget):
    """
    首页的欢迎界面
    """

    # 是否可以画了
    canDraw = False
    imgData = ''
    currDateTime = ''
    currDate = ''
    currTime = ''

    def __init__(self):
        super().__init__()
        self.welcomeWidget = _WelcomeWidget()
        self.welcomeWidget.setupUi(self)
        self.welcomeWidget.init()
        self.painter = QPainter()
        self.timer = QTimer()
        self.animDateTime = QPropertyAnimation(self.welcomeWidget.widgetDateTime, b"pos")
        self.animWidget = QPropertyAnimation(self.welcomeWidget.widget, b"pos")
        self.animVersion = QPropertyAnimation(self.welcomeWidget.widgetVersion, b"pos")
        self.initAppearance()
        pass

    def initAppearance(self):
        # 开启线程获取欢迎图片
        t = threading.Thread(target=self.getImgData, name='', )
        t.start()

        # 系统时间
        self._timerUpDate()
        self.timer.timeout.connect(self._timerUpDate)
        self.timer.start(1000)

        # 动图
        # movie = QMovie('resource/imgs/gif1.gif')
        # self.welcomeWidget.lblGif.setMovie(movie)
        # self.welcomeWidget.lblGif.setScaledContents(True)
        # movie.start()

        # 设置动画
        self.initAnimation()
        pass

    def initAnimation(self):
        # 启动动画
        QTimer.singleShot(500, self.doAnim)
        pass

    def doAnim(self):
        # 移动动画
        self.animDateTime.setDuration(1000)
        self.animDateTime.setStartValue(self.welcomeWidget.widgetDateTime.pos())
        self.animDateTime.setEndValue(QPoint(650, 20))
        self.animDateTime.start()
        self.animWidget.setDuration(1000)
        self.animWidget.setStartValue(self.welcomeWidget.widget.pos())
        self.animWidget.setEndValue(QPoint(20, 360))
        self.animWidget.start()
        self.animVersion.setDuration(1000)
        self.animVersion.setStartValue(self.welcomeWidget.widgetVersion.pos())
        self.animVersion.setEndValue(QPoint(20, 20))
        self.animVersion.start()
        self.animVersion.finished.connect(lambda: print('动画完成'))
        pass

    def _timerUpDate(self):
        self.currDateTime = QDateTime.currentDateTime()
        self.currDate = self.currDateTime.toString("yyyy年MM月dd日")
        self.currTime = self.currDateTime.toString("hh:mm:ss")
        self.welcomeWidget.lblDate.setText(self.currDate)
        self.welcomeWidget.lblTime.setText(self.currTime)

    def getImgData(self):
        # req = requests.get('https://cn.bing.com/th?id=OHR.WatChaloem_ZH-CN8722271527_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp')
        # self.imgData = QPixmap()
        # self.imgData.loadFromData(req.content)
        # print('获取完毕')
        self.imgData = QPixmap('resource/imgs/welcome/welcome_01.png')
        self.canDraw = True
        self.update()
        # self.imgData = ''
        pass

    def paintEvent(self, event):
        if self.canDraw:
            self.painter.begin(self)
            self.painter.drawPixmap(0, 0, self.width(), self.height(), self.imgData)
            self.painter.end()

    pass
