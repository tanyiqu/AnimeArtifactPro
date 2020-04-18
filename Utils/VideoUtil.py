import webbrowser
from subprocess import call
import threading
import R
from Configuration import Configuration

config = Configuration()
player = config.player_path


def play(link):
    """
    调用potplayer播放视频
    :param link: 视频链接
    :return: None
    """
    # 如果没有路径，返回-1
    if player is None:
        return -1
    # 开启线程播放
    # 判断一下能不能用potplayer播放
    if link[-5:].lower() == '.m3u8':
        broswerLk = (R.string.M3U8_API + '{}').format(link)
        webbrowser.open_new(broswerLk)
        return 0
    t = threading.Thread(target=_play_, name='播放', args=(link,))
    t.start()
    return 0
    pass


def _play_(link):
    call([player, link])
    pass
