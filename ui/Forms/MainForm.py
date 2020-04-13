from PyQt5.QtWidgets import QWidget

# noinspection PyProtectedMember
from ui.Forms._Forms._MainForm import _MainForm


class MainForm(QWidget):
    """
    主窗口类
    """

    def __init__(self):
        super().__init__()
        self.mainForm = _MainForm()
        self.mainForm.setupUi(self)
        self.mainForm.init(self)
        pass

    pass