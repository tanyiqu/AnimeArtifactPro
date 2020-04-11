import requests

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
    return resp.content.decode('utf-8')
    pass
