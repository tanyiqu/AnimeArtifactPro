from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFocusEvent
from PyQt5.QtWidgets import QLineEdit


class SearchBarWidget(QLineEdit):
    """
    输入框
    为了实现获取焦点是全选
    """

    def __init__(self):
        super().__init__()
        self.setText('辉夜大小姐')
        self.setMinimumHeight(38)
        self.setStyleSheet("""
            QLineEdit{
            background-color: #393942;
            color: #bababa;
            border-top-left-radius : 19px;
            border-bottom-left-radius : 19px;
            border-top-right-radius : 0;
            font: 13pt "微软雅黑";
            padding-left:15px;
            }
            QLineEdit:hover{
            background-color: #373036;
            border: 1px solid #393942;
            }""")

        pass

    def focusInEvent(self, event: QFocusEvent):
        super().focusInEvent(event)
        QTimer.singleShot(0, self.selectAll)
        pass

    pass
