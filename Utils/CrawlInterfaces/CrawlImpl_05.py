import requests
import re
import json

from Utils.CrawlUtil import CrawlUtil

"""
爬取资源网
http://www.zuidazy4.com/
"""


class CrawlImpl_05(CrawlUtil):
    URL = 'http://www.zuidazy4.com/index.php'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4287.0 Safari/537.36 Edg/88.0.673.0'
    }

    def search(self, searchword):
        url = 'http://www.zuidazy4.com/index.php'
        params = {
            'm': 'vod-search',
            'wd': searchword,
            'submit': 'search'
        }

        resp = requests.get(url=url, params=params, headers=self.headers)

        txt = resp.text

        reg = '<li><span class="tt"></span><span class="xing_vb4"><a href="(.*?)" target="_blank">(.*?)<span>(.*?)</span></a></span> <span class="xing_vb5">(.*?)</span> <span class="xing_vb6">(.*?)</span></li>'

        res = re.findall(reg, txt)

        if len(res) > 16:
            res = res[0:16]
            pass

        result = []
        for item in res:
            result.append({
                'url': 'http://www.zuidazy4.com/' + item[0],
                'cover': 'cover',
                'title': item[1],
                'latest': item[2],
                'area': item[3],
            })
            pass

        # 开启线程获取封面地址
        for item in result:
            
            pass

        return result.__str__().replace('\'', '\"')
        pass

    def parseSearchResult(self, jsonobj):
        # print('jsonobj', jsonobj)
        print('进入解析')
        result = []
        for item in jsonobj:
            result.append({
                'url': item['url'],
                'cover': item['cover'],
                'title': item['title'],
                'latest': item['latest'],
                'area': item['area'],
                'time': '时间',
                'stars': '演员'
            })
            pass
        return result
        pass

    def detail(self, func, url):
        result = {}

        resp = requests.get(url=url, headers=self.headers)
        txt = str(resp.text)

        txt = txt.replace(' ', '').replace('\n', '')

        reg = '<divid="play_1">(.*?)</div'
        res = re.findall(reg, txt)[0]

        reg = r'<li><inputtype="checkbox"name="copy_sel"value=".*?"checked=""/>(.*?)\$(.*?)</li>'

        res = re.findall(reg, res)

        for i in range(1, len(res) + 1):
            value = [res[i - 1][0], res[i - 1][1]]
            result.update({i: value})
            pass
        return result

    def getVideoUrl(self, url):
        # 因为url已经是m3u8的直链了，所以直接返回
        return url
        pass

    def getCover(self, url):
        txt = requests.get(url=url, headers=self.headers).text
        txt = txt.replace(' ', '').replace('\n', '')
        reg = r'<imgclass="lazy"src="(.*?)"alt='
        res = re.findall(reg, txt)[0]
        return res
        pass


if __name__ == '__main__':
    crawl = CrawlImpl_05()
    crawl.search('legal')
    pass
