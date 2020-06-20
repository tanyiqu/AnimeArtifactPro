import re
import time

import requests

from Utils.CrawlUtil import CrawlUtil


class CrawlImpl_01(CrawlUtil):
    """
    第一个接口的实现类
    接口爬取目标：http://susudm.com/
    """
    URL = 'http://testsea.diyiwl.wang/ssszz.php'

    def search(self, searchword):
        params = {
            'top': '10',
            'q': searchword,
            'dect': '0'
        }
        resp = requests.get(self.URL, params=params)
        return str(resp.content.decode('utf_8_sig')).strip()
        pass

    def parseSearchResult(self, json):
        result = []
        for o in json:
            obj = {}
            url = o['url']
            if re.match('^/.*?/$', o['url']):
                url = 'http://susudm.com' + o['url']
                pass
            obj.update({'url': url})
            obj.update({'cover': o['thumb']})
            obj.update({'title': o['title']})
            obj.update({'latest': o['lianzaijs']})
            obj.update({'area': o['area']})
            obj.update({'time': o['time']})
            obj.update({'stars': o['star']})
            result.append(obj)
        return result
        pass

    def detail(self, log, url):
        print('目标链接：', url)
        # 获取后缀路径
        path = re.findall('com(.*?)$', url)[0]
        print('后缀路径：', path)
        htmlSrc = self.getHtmlSrc(url)
        episodeDir = self.getEpisodeDir(htmlSrc, path)
        num = len(episodeDir)
        # 获取总集数（含备用链接，结果可能比正片集数多）
        log('正在获取总集数（含备用链接，结果可能比正片集数多）')
        print(episodeDir)
        # 获取js文件
        log('正在获取js文件...')
        jsSrc = self.getJsSrc(url)
        print('jsSrc：', jsSrc)
        # 获取链接后缀
        jsonLinkDir = self.getJsonLinkDir(jsSrc, num)
        # print('jsonLinkDir：', jsonLinkDir)
        detailResult = {}
        for i in range(1, num + 1):
            value = [episodeDir[i], jsonLinkDir[i]]
            # detailResult.update({episodeDir[i]: jsonLinkDir[i]})
            detailResult.update({i: value})
        # 整合成{集数名:json链接}
        # print('最终整合：', detailResult)
        return detailResult
        pass

    def getVideoUrl(self, jsonLink):
        """
        获取真实的播放链接
        :param jsonLink: json文件url
        :return: None
        """
        jsonLink = jsonLink.replace('http://test.1yltao.com', 'http://test.1yltao.com:8022')

        temp_url = re.findall('url=(.*?)', jsonLink)[0]
        myheaders = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Host': 'test.1yltao.com',
            'Origin': 'http://test2.diyiwl.wang',
            'Referer': 'http://test2.diyiwl.wang/1717yun/mytest.php?url={}'.format(temp_url),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36 Edg/81.0.416.41'
        }
        s = requests.get(jsonLink, headers=myheaders).text
        s = re.findall('"url":"(.*?)"', s)[0]
        s = s.replace('\\', '')
        return s
        pass

    # html源码
    def getHtmlSrc(self, url):
        """
        爬取指定url的源码
        :param url:指定url
        :return:源码
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36 Edg/81.0.416.41'
        }
        resp = requests.get(url, headers=headers)
        src = resp.content
        src = src.decode('utf-8')
        return src

    # {第几集:每集的名字}
    def getEpisodeDir(self, src, path):
        """
        获取总集数
        :param src: 源码
        :param path: 番剧的后缀
        :return: 字典：{第几集:每集的名字}
        """
        episodeDir = {}
        num = 1
        while True:
            # 拼接链接 /acg/2130/1.html
            episodeUrl = '%s%d.html' % (path, num)
            reg = '<a href="%s">(.*?)</a>' % episodeUrl
            result = re.search(reg, src)
            if result:
                # 匹配成功
                ename = re.findall(reg, src)[0]
                episodeDir.update({num: ename})
                pass
            else:
                # 匹配失败
                break
                pass
            num += 1
        return episodeDir

    # 存放播放链接后缀的js文件
    def getJsSrc(self, url):
        """
        获取存放 视频链接后缀 的js文件的源码
        :param url: url http://susudm.com/acg/2130/
        :return:  js源码
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36 Edg/81.0.416.41'
        }
        url += '1.html'
        print('url：：', url)
        src = requests.get(url, headers=headers).text

        # with open('C:/Users/Tanyiqu/Desktop/a.html', 'w', encoding='utf-8') as f:
        #     f.write(src)
        #     pass

        # reg = '</head><script type="text/javascript" src="(.*?)"></script>'
        reg = '<script type="text/javascript" src="(.*?)"></script>'
        # 获取js文件文件的链接
        jsLink = re.findall(reg, src)[0]
        print('jsLink：' + jsLink)
        # 获取js源码
        jsSrc = requests.get(jsLink, headers=headers).text
        return jsSrc

    # 获取json文件的链接
    def getJsonLinkDir(self, jsSrc, num):
        """
        拼接存有播放链接的json文件的链接，返回{第几集:json链接}
        此操作最耗时，最好能有提示信息
        :param jsSrc: js源码
        :param num:  集数
        :return: 字典 {第几集:json链接}
        """
        jsonLinkDir = {}
        # print(num)
        # print('jsSrc:', jsSrc)
        # 依次拼接链接
        for i in range(1, num + 1):
            print('第', i, '次')
            reg = r'\[%d\]="(.*?),' % i
            # print('reg:', reg2)
            # 匹配所有后缀
            suffixes = re.findall(reg, jsSrc)
            print(suffixes)
            suffix = ''
            # 打擂台来获取优先级最高的后缀
            for s in suffixes:
                if self.getSuffixPriority(s) < self.getSuffixPriority(suffix):
                    suffix = s
                pass
            print('取：', suffix)
            jsonLink = 'http://test.1yltao.com/testapi888.php?time={}&url={}'.format(int(time.time()), suffix)
            jsonLinkDir.update({i: jsonLink})
        return jsonLinkDir

    # 获取后缀的优先级
    def getSuffixPriority(self, suffix):
        """
        获取后缀的优先级
        # 1. '1097_5382ce5f262e4ddbaab3c61fa73cdbbb'
        # 2. 'xxxxx.mp4'
        # 3. 'xxxxx.m3u8'
        # 4. 'xxxxx.html
        # 5. 其他
        # 6. 无后缀
        :param suffix: 后缀
        :return: 优先级
        """
        suffix = suffix.strip()
        # 6. 无后缀
        if suffix == '':
            return 6
        # 1. '1097_5382ce5f262e4ddbaab3c61fa73cdbbb'
        if len(suffix) == 37 and suffix[4] == '_':
            return 1
        # 2. 'xxxxx.mp4'
        if suffix[-4:].lower() == '.mp4':
            return 2
        # 3. 'xxxxx.m3u8'
        if suffix[-5:].lower() == '.m3u8':
            return 3
        # 4. 'xxxxx.html
        if suffix[-5:].lower() == '.html':
            return 4
        return 5
