"""
获取指定url链接的源码
"""
import requests


def getSrc(url, headers=None, decode='utf-8'):
    resp = requests.get(url, headers=headers)
    return resp.content.decode(decode)
    pass
