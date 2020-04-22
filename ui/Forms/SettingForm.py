import threading
import webbrowser
from subprocess import call

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QFileDialog

import R
from Configuration import Configuration
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

        self.settingForm.btnCheckUpdate.clicked.connect(lambda: webbrowser.open_new(R.string.DOWNLOAD_LINK))

        self.settingForm.btnTestPlayer.clicked.connect(self._testPlayer)
        self.settingForm.btnTestPlayer2.clicked.connect(self._testPlayer2)
        self.settingForm.btnTestIDM.clicked.connect(self._testIDM)

        self.settingForm.btnFinished.clicked.connect(self._finish)

        self.settingForm.btnChoosePlayer.clicked.connect(self._choosePlayer)
        self.settingForm.btnChoosePlayer2.clicked.connect(self._choosePlayer2)
        self.settingForm.btnChooseIDM.clicked.connect(self._chooseIDM)

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
        self.config.player_pot_path = self.settingForm.lblPlayer.text().strip()
        self.config.player_vlc_path = self.settingForm.lblPlayer2.text().strip()
        self.config.idm_path = self.settingForm.lblIDM.text().strip()
        self.config.showClosingWarning = self.settingForm.checkClosingWarning.isChecked()
        self.config.play_sound = self.settingForm.checkPlaySound.isChecked()
        self.config.checkUpdate = self.settingForm.checkCheckUpdate.isChecked()
        self.config.save()
        pass

    def _testPlayer(self):
        path = self.settingForm.lblPlayer.text()
        t = threading.Thread(target=lambda: call(path), name='testPlay')
        t.start()
        print('测试player', path)
        pass

    def _testPlayer2(self):
        path = self.settingForm.lblPlayer2.text()
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
            self.settingForm.lblPlayer.setText(fileName_choose)
        pass

    def _choosePlayer2(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择播放器',
                                                                './',
                                                                "播放器 (*exe);")
        if fileName_choose != '':
            self.settingForm.lblPlayer2.setText(fileName_choose)
        pass

    def _chooseIDM(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                '选择下载器',
                                                                './',
                                                                "播放器 (*exe);")
        if fileName_choose != '':
            self.settingForm.lblIDM.setText(fileName_choose)
        pass

    def loadConfig(self):
        self.settingForm.txtUserName.setText(self.config.user_name)
        self.settingForm.lblPlayer.setText(self.config.player_pot_path)
        self.settingForm.lblPlayer2.setText(self.config.player_vlc_path)
        self.settingForm.lblIDM.setText(self.config.idm_path)
        self.settingForm.checkClosingWarning.setChecked(self.config.showClosingWarning)
        self.settingForm.checkPlaySound.setChecked(self.config.play_sound)
        self.settingForm.checkCheckUpdate.setChecked(self.config.checkUpdate)
        pass

    pass
