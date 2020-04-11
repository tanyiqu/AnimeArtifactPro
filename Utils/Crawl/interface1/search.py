import requests
import re
from Configuration import Configuration

# 使用接口1搜索

url = 'http://testsea.diyiwl.wang/ssszz.php'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Host': 'testsea.diyiwl.wang',
    'Referer': 'http://susudm.com/search.php',
    'Connection': 'keep-alive',
    'Origin': 'http://susudm.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.50',
}


def search(searchword):
    params = {
        'top': '10',
        'q': searchword,
        'dect': '0'
    }
    resp = requests.get(url, params=params)
    return str(resp.content.decode('utf_8_sig')).strip()
    pass


def parse(json):
    """
    解析json成app标准的数组
    :param json: json
    :return: app标准的数组
    """
    result = []
    for o in json:
        obj = {}
        url = o['url']
        if re.match('^/.*?/$', o['url']):
            url = Configuration.getInstance().url_header + o['url']
            pass
        obj.update({'url': url})
        obj.update({'cover': o['thumb']})
        obj.update({'title': o['title']})
        obj.update({'latest': o['lianzaijs']})
        result.append(obj)
    return result
    pass
