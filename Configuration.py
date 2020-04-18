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

    # 基本上不会变动的变量
    user_name = 'Tanyiqu'   # 用户的昵称

    # 变量
    anim_duration = 600     # 欢迎动画持续时长 ms
    curr_interface = 1      # 当前调用的接口
    player_path = 'D:/PotPlayer/PotPlayerMini64.exe'
    idm_path = None

    # 是否标志
    play_anim = True            # 播放欢迎动画
    play_sound = True           # 播放音效
    showClosingWarning = False  # 显示警告框，抓取链接中的警告还是要显示

    def __init__(self):
        pass
