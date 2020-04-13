import webbrowser
from subprocess import call
import threading
import R

player = 'D:/PotPlayer/PotPlayerMini64.exe'


def play(link):
    """
    调用potplayer播放视频
    :param link: 视频链接
    :return: None
    """
    # 开启线程播放
    # 判断一下能不能用potplayer播放
    if link[-5:].lower() == '.m3u8':
        broswerLk = (R.string.M3U8_API + '{}').format(link)
        webbrowser.open_new(broswerLk)
        return
    t = threading.Thread(target=_play_, name='播放', args=(link,))
    t.start()
    pass


def _play_(link):
    call([player, link])
    pass
