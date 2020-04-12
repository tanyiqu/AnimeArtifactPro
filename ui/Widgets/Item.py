import threading

import requests
from PyQt5.QtGui import QPixmap

import R
from ui.ui_designer.ui_file.ui_widget_item import Ui_item


class Item(Ui_item):

    def __init__(self, url, title, cover, latest):
        self.url = url
        self.title = title
        self.cover = cover
        self.latest = latest
        pass

    def init(self, item):
        # 设置标题
        self.lblTitle.setText(self.title)
        # 设置标题提示
        self.lblTitle.setToolTip(self.title)
        # 设置最近集数
        if self.latest.strip() == R.string.NONE:
            pass
        else:
            self.lblLatest.setText('最新至：' + self.latest)
            pass
        # 设置封面 在线程里面设置，防止主线程卡顿
        t = threading.Thread(target=self._setCover, name='', args=(self.lblCover, self.cover,))
        t.start()
        # item.clicked.connect(lambda: print('按下'))
        # self.widget.clicked.connect(lambda: print('按下'))
        pass

    def _setCover(self, lbl, url):
        req = requests.get(url)
        photo = QPixmap()
        photo.loadFromData(req.content)
        lbl.setScaledContents(True)
        lbl.setPixmap(photo)
        pass

    pass
