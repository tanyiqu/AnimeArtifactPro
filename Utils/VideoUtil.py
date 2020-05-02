import webbrowser
from subprocess import call
import threading
import R
from Configuration import Configuration

# config = Configuration()
# player = config.player_path


def play(link):
    """
    调用potplayer播放视频
    :param link: 视频链接
    :return: None
    """

    # 处理m3u8链接
    if link[-5:].lower() == '.m3u8':
        # 判断是网页解析还是vlc解析
        if Configuration().broswer_decode_m3u8:
            broswerLk = (R.string.M3U8_API + '{}').format(link)
            webbrowser.open_new(broswerLk)
            return
        else:
            player = Configuration().player_vlc_path
        pass
    # mp4播放链接
    elif (link[-4:].lower() == '.mp4') or ('.mp4' in link.lower()):
        player = Configuration().player_pot_path
        pass
    # 处理其他链接
    else:
        broswerLk = (R.string.M3U8_API + '{}').format(link)
        webbrowser.open_new(broswerLk)
        return
        pass
    t = threading.Thread(target=_play_, name='播放', args=(link, player,))
    t.start()
    return 0
    pass


def _play_(link, player):
    call([player, link])
    pass
