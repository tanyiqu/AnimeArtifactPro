import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFileDialog

import Utils
from Configuration import Configuration
from ui.ui_designer.ui_file.uic_initDialog import Ui_initDialog


class InitDialog(QDialog):
    """
    注册对话框
    用于第一次打开app时进行一些设置
    """

    def __init__(self):
        super().__init__()
        self.config = Configuration()
        self.initForm = Ui_initDialog()
        self.initForm.setupUi(self)
        # 设置成只有关闭按钮
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        # 图标
        self.setWindowIcon(QIcon('resource/imgs/logo.png'))

        # 连接信号槽
        self.do_connect()
        pass

    def do_connect(self):
        self.initForm.btnFinished.clicked.connect(self._finished)
        self.initForm.btnChoosePlayer.clicked.connect(self._choosePlayer)
        self.initForm.btnChooseIDM.clicked.connect(self._chooseIDM)
        pass

    def _choosePlayer(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择播放器',
                                                                './',
                                                                "播放器 (*exe);")
        if fileName_choose != '':
            self.initForm.lblPlayer.setText(fileName_choose)
        pass

    def _chooseIDM(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择下载器',
                                                                './',
                                                                "下载器 (*exe);")
        if fileName_choose != '':
            self.initForm.lblIDM.setText(fileName_choose)
        pass

    def _finished(self):
        # 记录三个值
        user_name = self.initForm.txtUserName.text()
        player = self.initForm.lblPlayer.text()
        idm = self.initForm.lblIDM.text()

        print(user_name, player, idm)

        if user_name.strip() == '':
            user_name = 'Master'
        if player == "无":
            player = None
        if idm == "无":
            idm = None
        self.config.user_name = user_name.strip()
        self.config.player_pot_path = player
        self.config.idm_path = idm

        self.config.first_open = False
        self.config.save()
        Utils.restart_program()
        pass

    def _closeApp(self):
        # noinspection PyProtectedMember
        os._exit(0)
        pass

    pass
