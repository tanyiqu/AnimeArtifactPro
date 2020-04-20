import re
import threading
from subprocess import call

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QFileDialog

from Configuration import Configuration
from Utils import TextUtil
from ui.ui_designer.ui_file.uic_batchDownloadForm import Ui_batchDownloadForm


class BatchDownloadForm(QWidget):
    links = path = TextUtil.get_desktop() + '/download.txt'
    dir = ''

    def __init__(self):
        super().__init__()
        self.batchDownloadForm = Ui_batchDownloadForm()
        self.batchDownloadForm.setupUi(self)
        self.initAppearance()

        self.batchDownloadForm.btnChooseDir.clicked.connect(self._chooseDir)
        self.batchDownloadForm.btnOK.clicked.connect(self.finished)
        self.batchDownloadForm.btnCheckIDM.clicked.connect(self._checkIDM)
        self.batchDownloadForm.btnCheckLinks.clicked.connect(self._checkLinks)

        pass

    def initAppearance(self):
        # 设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        pass

    def _chooseDir(self):
        self.dir = QFileDialog.getExistingDirectory(self,
                                                    "选取文件夹",
                                                    TextUtil.get_desktop())
        if self.dir == '':
            return
        self.batchDownloadForm.lblDir.setText(self.dir)
        pass

    def finished(self):
        if self.batchDownloadForm.lblDir.text() == '无':
            return
        t = threading.Thread(target=self._doBatch, name='doBatch')
        t.start()
        pass

    def _doBatch(self):
        f = open(self.links)
        lines = f.readlines()
        f.close()
        print(lines)
        self._checkIDM()
        for line in lines:
            line = line.strip()
            ls = re.split(r'@', line)
            name = ls[0] + '.mp4'
            link = ls[1]
            call([Configuration().idm_path, '/d', link, '/p', self.dir, '/f', name, '/n', '/a'])
            pass
        pass

    def _checkIDM(self):
        path = Configuration().idm_path
        t = threading.Thread(target=lambda: call(path), name='testIDM')
        t.start()
        pass

    def _checkLinks(self):
        t = threading.Thread(target=lambda: call(['notepad', self.links]), name='testLinks')
        t.start()
        pass

    pass
