"""
自定义信号
"""

from PyQt5.QtCore import QObject, pyqtSignal


class SearchFinish(QObject):
    """
    搜索完成
    """
    signal = pyqtSignal()
    pass


class ItemWidgetMouseRelease(QObject):
    """
    鼠标释放
    """
    signal = pyqtSignal()
    pass


class DetailFinish(QObject):
    """
    获取详情完成
    """
    signal = pyqtSignal()
    pass


class UpdateSignal(QObject):
    """
    准备更新
    """
    signal = pyqtSignal()
    pass
