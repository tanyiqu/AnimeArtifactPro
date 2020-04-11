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
