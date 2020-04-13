"""
供外部调用
"""

import Utils.Crawl.interface1


def search(searchword, interface):
    """
    使用第interface个接口执行查询操作
    :param searchword: 关键词
    :param interface: 接口
    :return: json格式的字符串
    """
    if interface == 1:
        return Utils.Crawl.interface1.search(searchword)
    pass


def parseSearchResult(json, interface):
    """
    解析json成app标准的数组
    [{
        url:url,
        cover:cover,
        title:title,
        latest:latest   最新集数（最新连载），可有可无
        area:area,      可有可无
        time:time,      可有可无
        stars:stars     可有可无
    }]
    :param json: json
    :param interface: 接口
    :return: app标准的数组
    """
    if interface == 1:
        return Utils.Crawl.interface1.parse(json)
    pass


def detail(url, func, interface):
    """
    获取详情
    {
        1: ['第1集'.'url'],
        2: ['第2集'.'url']
    }
    :param url: 链接
    :param func: 打印日志接口
    :param interface: 接口
    :return: 详情信息的字典
    """
    if interface == 1:
        return Utils.Crawl.interface1.detail(url, func)
    pass


def getVideoUrl(url, interface):
    """
    获取视频真实播放链接
    :param url: url
    :param interface: 接口
    :return: 真实播放链接
    """
    if interface == 1:
        return Utils.Crawl.interface1.getPlayLink(url)
    pass
