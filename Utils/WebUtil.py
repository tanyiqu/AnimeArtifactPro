import requests
from PyQt5.QtGui import QPixmap


def setLabelImg(lbl, url):
    """
    为QLabel设置网络图片
    :param lbl: label
    :param url: 图片url
    :return: None
    """
    req = requests.get(url)
    photo = QPixmap()
    photo.loadFromData(req.content)
    lbl.setScaledContents(True)
    lbl.setPixmap(photo)
    pass