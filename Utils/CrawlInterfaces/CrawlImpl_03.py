import re

import requests

from Utils.CrawlUtil import CrawlUtil


class CrawlImpl_03(CrawlUtil):
    """
    接口3，资源不太清晰
    """
    domain = 'https://www.5xdmw.com/'

    def search(self, searchword):
        result = []
        headers = {
            'Referer': 'https://www.5xdmw.com/index.php',
            'Host': 'www.5xdmw.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        params = {
            'searchword': searchword
        }
        url1 = 'https://www.5xdmw.com/search.php?'

        htmlsrc = requests.get(url1, params=params, headers=headers).text

        reg = '<div class="list pborder">.*?</div>(.*?)</div>'
        res = re.findall(reg, htmlsrc)[0]
        reg = '<li><a href="/(.*?)" target="_blank" title=".*?"><img src="(.*?)"/><p>(.*?)</p><p><font color="red">.*?</font>.*?</p></a></li>'
        res = re.findall(reg, res)
        for i in res:
            url = i[0]
            cover = i[1]
            title = i[2]
            d = {
                "url": self.domain + url,
                "cover": cover,
                "title": title
            }
            result.append(d)
            pass

        return result.__str__().replace('\'', '\"')

    pass

    def parseSearchResult(self, obj):
        length = len(obj)
        for i in range(0, length):
            obj[i].update({'url': obj[i]['url']})
            cover = obj[i]['cover']
            if 'https://img.5xdmw.com' in cover:
                pass
            else:
                cover = 'https://img.5xdmw.com' + cover
            obj[i].update({'cover': cover})
            # print('cover', obj[i]['cover'])
            obj[i].update({'title': obj[i]['title']})
            obj[i].update({'latest': ''})
            obj[i].update({'area': ''})
            obj[i].update({'time': ''})
            obj[i].update({'stars': ''})
            pass
        return obj
        # return []
        pass

    def detail(self, func, url):
        result = {}
        headers = {
            'Referer': 'https://www.5xdmw.com/index.php',
            'Host': 'www.5xdmw.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        htmlsrc = requests.get(url, headers=headers).content.decode('utf-8')
        # print(htmlsrc)
        # with open('b.html','w',encoding='utf-8') as f:
        #     f.write(htmlsrc)
        reg = '<div id="playerList1">(.*?)</div'
        res = re.findall(reg, htmlsrc)[0]
        reg = """<li><a title='.*?' href='(.*?)' target="_blank">(.*?)</a></li>"""
        res = re.findall(reg, res)
        length = len(res)
        for i in range(1, length + 1):
            li = [res[i - 1][1]]
            url = 'https://www.5xdmw.com' + res[i - 1][0]
            li.append(url)
            result.update({i: li})
            pass
        return result

    def getVideoUrl(self, url):
        headers = {
            'Referer': 'https://www.5xdmw.com/index.php',
            'Host': 'www.5xdmw.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        htmlsrc = requests.get(url, headers=headers).content.decode('utf-8')
        # print(htmlsrc)
        # with open('c.html','w',encoding='utf-8') as f:
        #     f.write(htmlsrc)
        reg = 'var now="(.*?)"'
        url = re.findall(reg, htmlsrc)[0]
        print("URL", url)
        return url

    def getAllLinks(self, result, func):
        pass
