import webbrowser

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

import R
from ui.ui_designer.ui_file.uic_updateForm import Ui_updateForm


class UpdateForm(QWidget):

    def __init__(self):
        super().__init__()

        self.updateForm = Ui_updateForm()
        self.updateForm.setupUi(self)
        self.initAppearance()

        self.updateForm.btnGet.clicked.connect(lambda: webbrowser.open_new(R.string.DOWNLOAD_LINK))
        self.updateForm.btnMore.clicked.connect(lambda: webbrowser.open_new(R.string.TUTORIAL))

        pass

    def initAppearance(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        pass
    pass