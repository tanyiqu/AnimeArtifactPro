import re
from urllib import parse

import requests

from Utils.CrawlUtil import CrawlUtil


class CrawlImpl_02(CrawlUtil):
    def search(self, searchword):
        domain = 'http://www.imomoe.in'
        searchword = parse.quote(searchword, encoding='gbk')
        url = 'http://www.imomoe.in/search.asp?searchword={}'.format(searchword)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.60'
        }
        resp = requests.post(url, headers=headers)
        text = resp.content.decode('gbk')
        # 获取搜索结果
        # 先获取结果数，为了去掉多余的推荐
        reg = '查到<em>(.*?)</em>部动漫'
        num = int(re.findall(reg, text)[0])
        reg = '<a href="(.*?)" target="_blank"><img src="(.*?)" alt="(.*?)" /></a>'
        ls = re.findall(reg, text)
        result = []
        for i in range(0, num):
            result.append(ls[i])
        # print(result)
        searchResult = []
        for r in result:
            d = {}
            d.update({"url": domain + r[0]})
            d.update({"cover": r[1]})
            d.update({"title": r[2]})
            searchResult.append(d)
            pass
        # print(searchResult)
        return searchResult.__str__().replace('\'', '\"')
        pass

    def parseSearchResult(self, obj):
        length = len(obj)
        for i in range(0, length):
            obj[i].update({'url': obj[i]['url']})
            obj[i].update({'cover': obj[i]['cover']})
            obj[i].update({'title': obj[i]['title']})
            obj[i].update({'latest': ''})
            obj[i].update({'area': ''})
            obj[i].update({'time': ''})
            obj[i].update({'stars': ''})
            pass
        return obj
        pass

    def detail(self, func, url):
        pass

    def getVideoUrl(self, url):
        pass

    def getAllLinks(self, result, func):
        pass
