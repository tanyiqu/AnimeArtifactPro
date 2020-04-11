"""
供外部调用
"""

import Utils.Crawl.interface1.search


def search(searchword, interface):
    """
    使用第interface个接口执行查询操作
    :param searchword: 关键词
    :param interface: 接口
    :return: json格式的字符串
    """
    if interface == 1:
        return Utils.Crawl.interface1.search.search(searchword)
    pass


def parseSearchResult(json, interface):
    """
    解析json成app标准的数组
    [{
        url:url,
        cover:cover,
        title:title,
        latest:latest   最新集数（最新连载），可有可无
    }]
    :param json: json
    :param interface: 接口
    :return: app标准的数组
    """
    if interface == 1:
        return Utils.Crawl.interface1.search.parse(json)
    pass
