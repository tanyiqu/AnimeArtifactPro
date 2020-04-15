
class Configuration:
    """
    全局配置类
    应该是单例模式的，暂时先不搞
    """

    # 目标网站域名 因为有些爬取的url没有域名，只有路径
    url_header = 'http://susudm.com'

    # 欢迎动画持续时长
    anim_duration = 800

    # 用户的昵称
    user_name = 'Tanyiqu'

    # 获取单例实例
    @classmethod
    def getInstance(cls):
        instance = Configuration()
        return instance
    pass