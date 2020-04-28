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
        print('text', text)
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
        try:
            domain = 'http://www.imomoe.in/'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.60'
            }
            # 获取源码
            resp = requests.get(url, headers=headers)
            text = resp.content.decode('gbk')
            # print(text)
            # 获取总集数（网页播放链接）
            reg = """<li><a title='.*?' href='(.*?)' target="_blank">(.*?)</a></li>"""
            ls = re.findall(reg, text)
            ls = self.trimList(ls)
            print('ls', ls)
            url = domain + ls[0][0]
            print(url)
            text = requests.get(url, headers=headers).content.decode('gbk')
            # print(text)
            reg = '<script type="text/javascript" src="/playdata(.*?)"></script>'
            url = re.findall(reg, text)[0]
            # print(url)

            jsLink = 'http://www.imomoe.in/playdata' + url

            print('jsLink', jsLink)
            text = requests.get(jsLink, headers=headers).text
            print(text)
            reg = "(http.*?)'"
            rs = re.findall(reg, text)
            print('rs', rs)
            # 拼接结果
            d = {}
            num = len(ls)
            print('ls', ls)
            print(len(ls))

            print('rs', rs)
            print(len(rs))
            for i in range(0, num):
                ll = [ls[i][1], rs[i]]
                d.update({i + 1: ll})
                pass
            return d
        except Exception as e:
            print('异常', e)
            func('暂无信息！')
            # func('不得不说这个网站（樱花动漫）真不咋地！有没有珍藏的网站可以私聊我！')
            func('暂无信息！')
            return []
        pass

    def getVideoUrl(self, url):
        url = url[:-4]
        print("2 URL", url)
        return url
        pass

    def getAllLinks(self, result, func):
        pass

    def trimList(self, obj):
        newObj = [obj[0]]
        n = 0
        flag = obj[0][1]
        length = len(obj)

        for i in range(1, length):
            if obj[i][1] == flag:
                break
            newObj.append(obj[i])
            pass
        print('flag', flag)
        return newObj
        pass
