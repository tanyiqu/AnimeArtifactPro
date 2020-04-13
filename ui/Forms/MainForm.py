# noinspection PyProtectedMember
from Utils.WebUtil import setLabelImg
from ui.Forms._Forms._MainForm import _MainForm
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import R


class MainForm(QWidget):
    """
    主窗口类
    """

    def __init__(self):
        super().__init__()
        self.mainForm = _MainForm()
        self.mainForm.setupUi(self)
        self.mainForm.init()
        # 初始化外观
        self.initAppearance()

        pass

    def initAppearance(self):
        # 标题
        self.setWindowTitle(R.string.APP_NAME)
        # 图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # 加载欢迎图片
        self.mainForm.lblWelcomeImg.setFixedSize(800,400)
        url = 'https://cn.bing.com//th?id=OHR.WatChaloem_ZH-CN8722271527_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'
        setLabelImg(self.mainForm.lblWelcomeImg, url)
        pass

    pass
