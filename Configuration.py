import json
import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Configuration(metaclass=SingletonType):
    """
    全局配置类
    单例模式
    """

    jsonPath = 'user data/config.json'

    # 基本上不会变动的变量
    user_name = 'Tanyiqu'   # 用户的昵称

    # 变量
    anim_duration = 600     # 欢迎动画持续时长 ms
    curr_interface = 1      # 当前调用的接口
    player_pot_path = None
    player_vlc_path = None
    idm_path = None

    # 是否标志
    first_open = True           # 首次打开App
    play_anim = True            # 播放欢迎动画
    play_sound = True           # 播放音效
    showClosingWarning = False  # 显示警告框，抓取链接中的警告还是要显示
    checkUpdate = True          # 检查更新
    broswer_decode_m3u8 = True  # 用浏览器解析m3u8
    broswer_decode_all = True   # 用浏览器解析所有连接

    def __init__(self):
        with open(self.jsonPath, encoding='utf-8') as f:
            self.obj = json.load(f)
            # print('obj', self.obj)
            pass
        self.first_open = self.obj['first_open']
        self.user_name = self.obj['user_name']
        self.anim_duration = self.obj['anim_duration']
        self.curr_interface = self.obj['curr_interface']
        self.player_pot_path = self.obj['player_pot_path']
        self.player_vlc_path = self.obj['player_vlc_path']
        self.idm_path = self.obj['idm_path']
        self.play_anim = self.obj['play_anim']
        self.play_sound = self.obj['play_sound']
        self.showClosingWarning = self.obj['showClosingWarning']
        self.checkUpdate = self.obj['checkUpdate']
        self.broswer_decode_m3u8 = self.obj['broswer_decode_m3u8']
        self.broswer_decode_all = self.obj['broswer_decode_all']
        pass

    # 保存设置到json
    def save(self):
        self.obj['first_open'] = self.first_open
        self.obj['user_name'] = self.user_name
        self.obj['anim_duration'] = self.first_open
        self.obj['curr_interface'] = self.curr_interface
        self.obj['player_vlc_path'] = self.player_vlc_path
        self.obj['player_pot_path'] = self.player_pot_path
        self.obj['idm_path'] = self.idm_path
        self.obj['play_anim'] = self.play_anim
        self.obj['play_sound'] = self.play_sound
        self.obj['showClosingWarning'] = self.showClosingWarning
        self.obj['checkUpdate'] = self.checkUpdate
        self.obj['broswer_decode_m3u8'] = self.broswer_decode_m3u8
        self.obj['broswer_decode_all'] = self.broswer_decode_all
        with open(self.jsonPath, 'w') as f:
            json.dump(self.obj, f)
            pass
        pass

    # 恢复默认数据
    def default(self):
        self.first_open = False
        self.user_name = 'Master'
        self.anim_duration = 600
        self.curr_interface = 1
        self.player_vlc_path = None
        self.player_pot_path = None
        self.idm_path = None
        self.play_anim = True
        self.play_sound = True
        self.showClosingWarning = True
        self.checkUpdate = False
        self.broswer_decode_m3u8 = True
        self.broswer_decode_all = True
        self.save()
        pass

    pass
