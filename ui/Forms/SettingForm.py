import random
import threading
import webbrowser
import shutil
from subprocess import call

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QFileDialog

import R
from Configuration import Configuration
from Utils import TextUtil
from ui.ui_designer.ui_file.uic_settingForm import Ui_settingForm


class SettingForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.settingForm = Ui_settingForm()
        self.settingForm.setupUi(self)
        self.config = Configuration()
        self.initAppearance()
        self.loadConfig()

        # 检查更新
        self.settingForm.btnCheckUpdate.clicked.connect(lambda: webbrowser.open_new(R.string.DOWNLOAD_LINK))
        # 配置exe
        self.settingForm.btnTestPlayerPot.clicked.connect(self._testPlayer)
        self.settingForm.btnTestPlayerVlc.clicked.connect(self._testPlayer2)
        self.settingForm.btnTestIDM.clicked.connect(self._testIDM)
        # 完成
        self.settingForm.btnFinished_1.clicked.connect(self._finish)
        # 选择exe
        self.settingForm.btnChoosePlayerPot.clicked.connect(self._choosePlayer)
        self.settingForm.btnChoosePlayerVlc.clicked.connect(self._choosePlayer2)
        self.settingForm.btnChooseIDM.clicked.connect(self._chooseIDM)
        # 切换背景
        self.settingForm.btnChangeBG.clicked.connect(self._changeBG)

        pass

    def initAppearance(self):
        # 设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        pass

    def _finish(self):
        self.save()
        self.close()
        self.parent.syncInterface()
        pass

    def save(self):
        print('点击完成')
        self.config.user_name = self.settingForm.txtUserName.text().strip()
        self.config.player_pot_path = self.settingForm.lblPlayerPot.text().strip()
        self.config.player_vlc_path = self.settingForm.lblPlayerVlc.text().strip()
        self.config.idm_path = self.settingForm.lblIDM.text().strip()
        self.config.showClosingWarning = self.settingForm.checkClosingWarning.isChecked()
        self.config.play_sound = self.settingForm.checkPlaySound.isChecked()
        self.config.checkUpdate = self.settingForm.checkCheckUpdate.isChecked()
        self.config.save()
        pass

    def _testPlayer(self):
        path = self.settingForm.lblPlayerPot.text()
        t = threading.Thread(target=lambda: call(path), name='testPlay')
        t.start()
        print('测试player', path)
        pass

    def _testPlayer2(self):
        path = self.settingForm.lblPlayerVlc.text()
        t = threading.Thread(target=lambda: call(path), name='testPlay')
        t.start()
        print('测试player', path)
        pass

    def _testIDM(self):
        path = self.settingForm.lblIDM.text()
        t = threading.Thread(target=lambda: call(path), name='testIDM')
        t.start()
        print('测试idm', path)
        pass

    def _choosePlayer(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择播放器',
                                                                './',
                                                                "播放器 (*exe);")
        if fileName_choose != '':
            self.settingForm.lblPlayerPot.setText(fileName_choose)
        pass

    def _choosePlayer2(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择播放器',
                                                                './',
                                                                "播放器 (*exe);")
        if fileName_choose != '':
            self.settingForm.lblPlayerVlc.setText(fileName_choose)
        pass

    def _chooseIDM(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择下载器',
                                                                './',
                                                                "播放器 (*exe);")
        if fileName_choose != '':
            self.settingForm.lblIDM.setText(fileName_choose)
        pass

    def _changeBG(self):
        # 选择图片
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择背景图',
                                                                TextUtil.get_desktop(),
                                                                "背景图（只支持png） (*png);")
        img_path = 'resource/imgs/welcome/welcome_01.png'
        # 备份原来的图片
        # 生成乱码后缀
        sur = ''.join(random.sample(
            ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
             'e', 'd', 'c', 'b', 'a'], 6))
        img_path_ = 'resource/imgs/welcome/welcome_01{}.png'.format(sur)
        shutil.copyfile(img_path, img_path_)
        # 复制选择的图片
        shutil.copyfile(fileName_choose, img_path)
        # 生效
        self.parent.syncInterface()
        pass

    def loadConfig(self):
        self.settingForm.txtUserName.setText(self.config.user_name)
        self.settingForm.lblPlayerPot.setText(self.config.player_pot_path)
        self.settingForm.lblPlayerVlc.setText(self.config.player_vlc_path)
        self.settingForm.lblIDM.setText(self.config.idm_path)
        self.settingForm.checkClosingWarning.setChecked(self.config.showClosingWarning)
        self.settingForm.checkPlaySound.setChecked(self.config.play_sound)
        self.settingForm.checkCheckUpdate.setChecked(self.config.checkUpdate)
        pass

    pass
