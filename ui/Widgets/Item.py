import threading

import R
from Utils.WebUtil import setLabelImg
from ui.ui_designer.ui_file.ui_widget_item import Ui_item


class Item(Ui_item):

    def __init__(self, url, title, cover, latest):
        self.url = url
        self.title = title
        self.cover = cover
        self.latest = latest
        pass

    def init(self):
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
        t = threading.Thread(target=setLabelImg, name='', args=(self.lblCover, self.cover,))
        t.start()
        pass

    pass
