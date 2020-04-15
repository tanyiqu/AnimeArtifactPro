import threading

import R
from Utils.WebUtil import setLabelImg
from ui.ui_designer.ui_file.uic_itemWidget import Ui_item


class _ItemWidget(Ui_item):

    def __init__(self, params):
        """
        :param params: {'url', 'title', 'latest' , 'area', 'time' , 'stars'}
        """
        self.params = params
        pass

    def init(self):
        # print('params', self.params)
        # 设置标题
        print(self.params['title'])
        self.lblTitle.setText(self.params['title'])
        # 设置标题提示
        self.lblTitle.setToolTip(self.params['title'])
        # 设置最近集数
        if self.params['latest'].strip() == R.string.NONE:
            pass
        else:
            self.lblLatest.setText('最新至：' + self.params['latest'])
            pass
        # 设置封面 在线程里面设置，防止主线程卡顿
        t = threading.Thread(target=setLabelImg, name='', args=(self.lblCover, self.params['cover'],))
        t.start()
        pass

    pass
