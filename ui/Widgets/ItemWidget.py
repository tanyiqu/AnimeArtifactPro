"""
实现了Item的自定义QWidget类
为了实现点击事件
"""

from PyQt5.QtWidgets import QWidget

from Signals import ItemWidgetMouseRelease
from ui.Widgets.Item import Item


class ItemWidget(QWidget):

    # elapse = 0
    # start = 0
    # end = 0

    def __init__(self, params):
        super().__init__()
        self.item = Item(params)
        self.item.setupUi(self)
        self.item.init()
        self.itemWidgetMouseRelease = ItemWidgetMouseRelease()
        pass

    # # 鼠标按下
    # def mousePressEvent(self, event):
    #     print(event.buttons())
    #     print(Qt.LeftButton)
    #     if event.buttons() == Qt.LeftButton:
    #         self.start = time.time()
    #         pass
    #     event.accept()
    #     pass

    # 鼠标抬起
    def mouseReleaseEvent(self, event):
        self.itemWidgetMouseRelease.signal.emit()
        pass

    pass
