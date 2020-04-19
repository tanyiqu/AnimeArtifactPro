from PyQt5.QtWidgets import QWidget

from ui.ui_designer.ui_file.uic_logsForm import Ui_logsForm


class LogsForm(QWidget):

    def __init__(self):
        super().__init__()
        self.logsForm = Ui_logsForm()
        self.logsForm.setupUi(self)

        pass

    pass