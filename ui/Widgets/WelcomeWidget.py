import threading

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton


class WelcomeWidget(QWidget):
    """
    首页的欢迎界面
    """


    # 是否可以画了
    canDraw = False
    imgData = ''

    def __init__(self):
        super().__init__()
        self.painter = QPainter()
        # self.painter.setPen()
        # self.layout = QGridLayout()
        # self.setLayout(self.layout)
        # self.layout.addWidget(QPushButton('123'))
        # 开启线程获取欢迎图片
        t = threading.Thread(target=self.getImgData, name='', )
        t.start()
        pass

    def getImgData(self):
        # req = requests.get('https://cn.bing.com/th?id=OHR.WatChaloem_ZH-CN8722271527_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp')
        # self.imgData = QPixmap()
        # self.imgData.loadFromData(req.content)
        self.imgData = QPixmap('resource/imgs/welcome.jpg')
        self.canDraw = True
        self.update()
        # self.imgData = ''
        pass

    def paintEvent(self, event):
        if self.canDraw:
            self.painter.begin(self)
            # self.painter.drawLine(0, 0, self.width(), self.height())
            self.painter.drawPixmap(0, 0, self.width(), self.height(), self.imgData)
            self.painter.end()

    pass
