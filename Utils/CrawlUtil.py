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
