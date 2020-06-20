import re
import time

import requests

from Utils.CrawlUtil import CrawlUtil


class CrawlImpl_04(CrawlUtil):
    """
    第一个接口的实现类
    接口爬取目标：http://susudm.com/
    """
    URL = 'http://www.zuidazy5.com/index.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.zuidazy5.com',
        'Host': 'www.zuidazy5.com',
        'Referer': 'http://www.zuidazy5.com/',
        'Cookie': 'UM_distinctid=172878a738d625-03f268198f8d39-376b4502-1fa400-172878a738e7c9; mac_history=%7Bvideo%3A%5B%7B%22name%22%3A%22%u5C11%u5973%u7684%u6447%u66F3%22%2C%22link%22%3A%22/%3Fm%3Dvod-detail-id-76239.html%22%2C%22typename%22%3A%22%u798F%u5229%u7247%22%2C%22typelink%22%3A%22/%3Fm%3Dvod-type-id--pg-1.html%22%2C%22pic%22%3A%22upload/vod/2020-01-05/202001051578199499.png%22%7D%5D%7D; PHPSESSID=8or2tl6ptmrc557r7fhgervt02; CNZZDATA1261462053=1172265067-1591408729-%7C1591873700'
        , 'Accept-Encoding': 'gzip, deflate'
    }

    def search(self, searchword):
        data = {
            'm': 'vod-search',
            'wd': searchword,
            'submit': 'search'
        }
        resp = requests.post(self.URL + '?m=vod-search', data=data, headers=self.headers)
        html = str(resp.content.decode('utf_8_sig')).strip()
        # print(html)
        uls = re.findall('<div class="xing_vb">.*?<ul.*?/ul>(.*?)</div>', html, re.S)
        # print(uls)
        videos = re.findall(
            '<ul>.*?<li>.*?<a href="(.*?)".*?>(.*?)<span>(.*?)</span>.*?<span.*?>(.*?)</span>.*?">(.*?)</span', uls[0],
            re.S)
        result = []
        for v in videos:
            # print(v)
            d = {}
            # 添加到字典
            d.update({'url': self.URL + v[0]})
            d.update({'title': v[1]})
            d.update({'latest': v[2]})
            d.update({'cover':'https://tu.tianzuida.com/pic/upload/vod/2020-01-02/202001021577922664.jpg'})

            d.update({'area': v[2]})
            # d.update({'type':v[3]})
            d.update({'time': v[4]})

            d.update({'stars': v[2]})
            result.append(d)
        print('result', result)
        return result.__str__().replace('\'', '\"')
        pass

    def parseSearchResult(self, json):
        return json
        pass

    def getVideoUrl(self, url):
        """
        获取真实的播放链接
        :param videolink: json文件url
        :return: None
        """
        resp = requests.get(url)
        html = resp.content.decode('utf-8')
        # print(html)
        # 播放源1
        play1 = re.findall('<div id="play_1">(.*?)</div>', html, re.S)
        play1List = re.findall('<li>.*?value="(.*?)".*?/>(.*?)\$.*?</li>', play1[0], re.S)
        # 播放源2
        play2 = re.findall('<div id="play_2">(.*?)</div>', html, re.S)
        play2List = re.findall('<li>.*?value="(.*?)".*?/>(.*?)\$.*?</li>', play2[0], re.S)
        # 下载源1
        download1 = re.findall('<div id="down_1">(.*?)</div>', html, re.S)
        downloadList = re.findall('<li>.*?value="(.*?)".*?/>(.*?)\$.*?</li>', download1[0], re.S)

        list = []
        list.append(play1List)
        list.append(play2List)
        list.append(downloadList)
        print(list)
        return list

#
# def detail(self, log, url):
#     print('目标链接：', url)
#     # 获取后缀路径
#     path = re.findall('com(.*?)$', url)[0]
#     print('后缀路径：', path)
#     htmlSrc = self.getHtmlSrc(url)
#     episodeDir = self.getEpisodeDir(htmlSrc, path)
#     num = len(episodeDir)
#     # 获取总集数（含备用链接，结果可能比正片集数多）
#     log('正在获取总集数（含备用链接，结果可能比正片集数多）')
#     print(episodeDir)
#     # 获取js文件
#     log('正在获取js文件...')
#     jsSrc = self.getJsSrc(url)
#     # print('jsSrc：', jsSrc)
#     # 获取链接后缀
#     jsonLinkDir = self.getJsonLinkDir(jsSrc, num)
#     # print('jsonLinkDir：', jsonLinkDir)
#     detailResult = {}
#     for i in range(1, num + 1):
#         value = [episodeDir[i], jsonLinkDir[i]]
#         # detailResult.update({episodeDir[i]: jsonLinkDir[i]})
#         detailResult.update({i: value})
#     # 整合成{集数名:json链接}
#     # print('最终整合：', detailResult)
#     return detailResult
#     pass
#

#
# # html源码
# def getHtmlSrc(self, url):
#     """
#     爬取指定url的源码
#     :param url:指定url
#     :return:源码
#     """
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36 Edg/81.0.416.41'
#     }
#     resp = requests.get(url, headers=headers)
#     src = resp.content
#     src = src.decode('utf-8')
#     return src
#
# # {第几集:每集的名字}
# def getEpisodeDir(self, src, path):
#     """
#     获取总集数
#     :param src: 源码
#     :param path: 番剧的后缀
#     :return: 字典：{第几集:每集的名字}
#     """
#     episodeDir = {}
#     num = 1
#     while True:
#         # 拼接链接 /acg/2130/1.html
#         episodeUrl = '%s%d.html' % (path, num)
#         reg = '<a href="%s">(.*?)</a>' % episodeUrl
#         result = re.search(reg, src)
#         if result:
#             # 匹配成功
#             ename = re.findall(reg, src)[0]
#             episodeDir.update({num: ename})
#             pass
#         else:
#             # 匹配失败
#             break
#             pass
#         num += 1
#     return episodeDir
#
# # 存放播放链接后缀的js文件
# def getJsSrc(self, url):
#     """
#     获取存放 视频链接后缀 的js文件的源码
#     :param url: url http://susudm.com/acg/2130/
#     :return:  js源码
#     """
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36 Edg/81.0.416.41'
#     }
#     url += '1.html'
#     src = requests.get(url, headers=headers).text
#     reg = '</head><script type="text/javascript" src="(.*?)"></script>'
#     # 获取js文件文件的链接
#     jsLink = re.findall(reg, src)[0]
#     print('jsLink：' + jsLink)
#     # 获取js源码
#     jsSrc = requests.get(jsLink, headers=headers).text
#     return jsSrc
#
# # 获取json文件的链接
# def getJsonLinkDir(self, jsSrc, num):
#     """
#     拼接存有播放链接的json文件的链接，返回{第几集:json链接}
#     此操作最耗时，最好能有提示信息
#     :param jsSrc: js源码
#     :param num:  集数
#     :return: 字典 {第几集:json链接}
#     """
#     jsonLinkDir = {}
#     # print(num)
#     # print('jsSrc:', jsSrc)
#     # 依次拼接链接
#     for i in range(1, num + 1):
#         print('第', i, '次')
#         reg = r'\[%d\]="(.*?),' % i
#         # print('reg:', reg2)
#         # 匹配所有后缀
#         suffixes = re.findall(reg, jsSrc)
#         print(suffixes)
#         suffix = ''
#         # 打擂台来获取优先级最高的后缀
#         for s in suffixes:
#             if self.getSuffixPriority(s) < self.getSuffixPriority(suffix):
#                 suffix = s
#             pass
#         print('取：', suffix)
#         jsonLink = 'http://test.1yltao.com/testapi888.php?time={}&url={}'.format(int(time.time()), suffix)
#         jsonLinkDir.update({i: jsonLink})
#     return jsonLinkDir
#
# # 获取后缀的优先级
# def getSuffixPriority(self, suffix):
#     """
#     获取后缀的优先级
#     # 1. '1097_5382ce5f262e4ddbaab3c61fa73cdbbb'
#     # 2. 'xxxxx.mp4'
#     # 3. 'xxxxx.m3u8'
#     # 4. 'xxxxx.html
#     # 5. 其他
#     # 6. 无后缀
#     :param suffix: 后缀
#     :return: 优先级
#     """
#     suffix = suffix.strip()
#     # 6. 无后缀
#     if suffix == '':
#         return 6
#     # 1. '1097_5382ce5f262e4ddbaab3c61fa73cdbbb'
#     if len(suffix) == 37 and suffix[4] == '_':
#         return 1
#     # 2. 'xxxxx.mp4'
#     if suffix[-4:].lower() == '.mp4':
#         return 2
#     # 3. 'xxxxx.m3u8'
#     if suffix[-5:].lower() == '.m3u8':
#         return 3
#     # 4. 'xxxxx.html
#     if suffix[-5:].lower() == '.html':
#         return 4
#     return 5


# class CrawlImpl_04(CrawlUtil):
#     domain = 'https://www.shiwutv.com'
#
#     def search(self, searchword):
#         url = 'https://www.shiwutv.com/vodsearch/-------------.html'
#         params = {
#             'wd': searchword
#         }
#         headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.24 Safari/537.36 Edg/83.0.478.18'
#         }
#         res = requests.get(url, params=params, headers=headers)
#         txt = res.content.decode('utf-8')
#
#         # 获取搜索结果的ul
#         reg1 = '<ul class="stui-vodlist__media col-pd clearfix">(.*?)</ul>'
#         txt = re.findall(reg1, txt)[0]
#         # print(txt)
#
#         # 获取每一个结果li
#         reg2 = '<li(.*?)</li>'
#         res = re.findall(reg2, str(txt))
#
#         # 获取每一个的详情
#         reg3 = 'class="v-thumb stui-vodlist__thumb lazyload" href="(.*?)" title="(.*?)" data-original="(.*?)">'
#         reg_area = '地区：.*?_blank">(.*?)</a>'
#         reg_time = '年份：.*?_blank">(.*?)</a>'
#         result = []
#         for i in res:
#             r = re.findall(reg3, i)[0]
#             d = {}
#             url = self.domain + r[0]
#             title = r[1]
#             cover = r[2]
#             if re.match('^/.*?$', r[2]):
#                 cover = self.domain + r[2]
#                 pass
#             area = re.findall(reg_area, i)[0]
#             time = re.findall(reg_time, i)[0]
#
#             # 添加到字典
#             d.update({'url': url})
#             d.update({'cover': cover})
#             d.update({'title': title})
#             d.update({'area': area})
#             d.update({'time': time})
#             result.append(d)
#             pass
#         return result.__str__().replace("'", '"').replace('\r', '')
#         pass
#
#     def parseSearchResult(self, obj):
#         length = len(obj)
#         for i in range(0, length):
#             obj[i].update({'cover': obj[i]['cover']})
#             # print('cover', obj[i]['cover'])
#             obj[i].update({'title': obj[i]['title']})
#             obj[i].update({'latest': ''})
#             obj[i].update({'area': obj[i]['area']})
#             obj[i].update({'time': obj[i]['time']})
#             obj[i].update({'stars': ''})
#             pass
#         return obj
#         pass
#
#     def detail(self, func, url):
#         d = {}
#         # 搞html源码
#         headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.24 Safari/537.36 Edg/83.0.478.18'
#         }
#         res = requests.get(url, headers=headers)
#         txt = res.content.decode('utf-8')
#         l1 = re.findall('(<div id="playlist1".*?</div>)', txt)[0]
#         l2 = re.findall('href="(.*?)">(.*?)</a>', l1)
#         length = len(l2)
#         for i in range(0, length):
#             ls = [l2[i][1], self.domain + l2[i][0]]
#             d.update({i + 1: ls})
#             pass
#         return d
#         pass
#
#     def getVideoUrl(self, url):
#         headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.24 Safari/537.36 Edg/83.0.478.18'
#         }
#         resp = requests.get(url, headers=headers)
#         txt = resp.content.decode('utf-8')
#         reg = 'var player_data={.*?"url":"(.*?)","url_next":.*?}'
#         u = re.findall(reg, txt)[0]
#         u = u.replace('\\', '')
#         return u
#         pass
