from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QWidget

import R
from ui.ui_designer.ui_file.uic_aboutForm import Ui_AboutForm


class AboutForm(QWidget):

    def __init__(self):
        super().__init__()
        self.aboutForm = Ui_AboutForm()
        self.aboutForm.setupUi(self)
        self.initAppearance()
        pass

    # 初始化外观
    def initAppearance(self):
        # 设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        # 设置标题
        self.setWindowTitle('关于 ' + R.string.APP_NAME)
        # 设置版本号
        self.aboutForm.lblVersion.setText(R.string.VERSION)
        # 设置logo
        pix = QPixmap('resource/imgs/logo.png')
        self.aboutForm.logo.setPixmap(pix)
        self.aboutForm.logo.setScaledContents(True)
        # 设置动图
        movie1 = QMovie('resource/imgs/gif1.gif')
        movie2 = QMovie('resource/imgs/gif2.gif')
        self.aboutForm.gif_1.setMovie(movie1)
        self.aboutForm.gif_2.setMovie(movie2)
        self.aboutForm.gif_1.setScaledContents(True)
        self.aboutForm.gif_2.setScaledContents(True)
        movie1.start()
        movie2.start()

    pass