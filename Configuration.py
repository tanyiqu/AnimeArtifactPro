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

    # 播放欢迎动画
    play_anim = True
    # 播放音效
    play_sound = True
    # 欢迎动画持续时长
    anim_duration = 600
    # 用户的昵称
    user_name = 'Tanyiqu'

    # 当前调用的接口
    curr_interface = 1

    def __init__(self):
        pass
