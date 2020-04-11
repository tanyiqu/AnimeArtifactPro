
class Configuration:
    """
    全局配置类
    应该是单例模式的，暂时先不搞
    """

    # 目标网站域名 因为有些爬取的url没有域名，只有路径
    url_header = 'http://susudm.com'

    @classmethod
    def getInstance(cls):
        instance = Configuration()
        return instance
    pass