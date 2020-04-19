from PyQt5.QtWidgets import QWidget

from ui.ui_designer.ui_file.uic_settingForm import Ui_settingForm


class SettingForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.settingForm = Ui_settingForm()
        self.settingForm.setupUi(self)
    pass