from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QLabel

import R
from ui.ui_designer.ui_file.uic_logsForm import Ui_logsForm


class LogsForm(QWidget):

    def __init__(self):
        super().__init__()
        self.logsForm = Ui_logsForm()
        self.logsForm.setupUi(self)

        self.initAppearance()
        self.initLogs()

        pass

    def initAppearance(self):
        # 设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        pass

    def initLogs(self):
        for log in R.string.UPDATE_LOG:
            text = '时间：' + log['time']
            text += '\n版本：' + log['version']
            text += '\n该版本总下载数：' + str(log['downloadNum'])
            text += '\n更新详情：'
            for detail in log['detail']:
                text += '\n' + detail
                pass
            lbl = QLabel(text)
            lbl.setFixedWidth(270)
            lbl.setStyleSheet('font: 10pt "微软雅黑";'
                              'padding: 3px;'
                              'border: 1px solid #7f7f7f;')
            lbl.setWordWrap(True)
            lbl.adjustSize()
            self.logsForm.layout.addWidget(lbl)
            pass
        self.logsForm.layout.addStretch()
        pass

    pass