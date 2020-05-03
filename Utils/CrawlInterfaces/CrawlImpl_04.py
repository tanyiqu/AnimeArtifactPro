import re

import requests

from Utils.CrawlUtil import CrawlUtil


class CrawlImpl_04(CrawlUtil):
    domain = 'https://www.shiwutv.com'

    def search(self, searchword):
        url = 'https://www.shiwutv.com/vodsearch/-------------.html'
        params = {
            'wd': searchword
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.24 Safari/537.36 Edg/83.0.478.18'
        }
        res = requests.get(url, params=params, headers=headers)
        txt = res.content.decode('utf-8')

        # 获取搜索结果的ul
        reg1 = '<ul class="stui-vodlist__media col-pd clearfix">(.*?)</ul>'
        txt = re.findall(reg1, txt)[0]
        # print(txt)

        # 获取每一个结果li
        reg2 = '<li(.*?)</li>'
        res = re.findall(reg2, str(txt))

        # 获取每一个的详情
        reg3 = 'class="v-thumb stui-vodlist__thumb lazyload" href="(.*?)" title="(.*?)" data-original="(.*?)">'
        reg_area = '地区：.*?_blank">(.*?)</a>'
        reg_time = '年份：.*?_blank">(.*?)</a>'
        result = []
        for i in res:
            r = re.findall(reg3, i)[0]
            d = {}
            url = self.domain + r[0]
            title = r[1]
            cover = r[2]
            if re.match('^/.*?$', r[2]):
                cover = self.domain + r[2]
                pass
            area = re.findall(reg_area, i)[0]
            time = re.findall(reg_time, i)[0]

            # 添加到字典
            d.update({'url': url})
            d.update({'cover': cover})
            d.update({'title': title})
            d.update({'area': area})
            d.update({'time': time})
            result.append(d)
            pass
        return result.__str__().replace("'", '"').replace('\r', '')
        pass

    def parseSearchResult(self, obj):
        length = len(obj)
        for i in range(0, length):
            obj[i].update({'cover': obj[i]['cover']})
            # print('cover', obj[i]['cover'])
            obj[i].update({'title': obj[i]['title']})
            obj[i].update({'latest': ''})
            obj[i].update({'area': obj[i]['area']})
            obj[i].update({'time': obj[i]['time']})
            obj[i].update({'stars': ''})
            pass
        return obj
        pass

    def detail(self, func, url):
        d = {}
        # 搞html源码
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.24 Safari/537.36 Edg/83.0.478.18'
        }
        res = requests.get(url, headers=headers)
        txt = res.content.decode('utf-8')
        l1 = re.findall('(<div id="playlist1".*?</div>)', txt)[0]
        l2 = re.findall('href="(.*?)">(.*?)</a>', l1)
        length = len(l2)
        for i in range(0, length):
            ls = [l2[i][1], self.domain + l2[i][0]]
            d.update({i + 1: ls})
            pass
        return d
        pass

    def getVideoUrl(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.24 Safari/537.36 Edg/83.0.478.18'
        }
        resp = requests.get(url, headers=headers)
        txt = resp.content.decode('utf-8')
        reg = 'var player_data={.*?"url":"(.*?)","url_next":.*?}'
        u = re.findall(reg, txt)[0]
        u = u.replace('\\', '')
        return u
        pass
