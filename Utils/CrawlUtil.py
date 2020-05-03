import re
import time
from abc import abstractmethod

from Utils import TextUtil


class CrawlUtil:
    """
    接口规范：
    不管接口内部是怎么实现的，
    总之，要提供外部这样的实现
    """

    @abstractmethod
    def search(self, searchword):
        """
        使用接口查询searchword
        :param searchword: 关键词
        :return: str 搜索结果
        //至少要包含这三个
        [{
        url:url,        整部动漫的url，如：http://susudm.com/acg/2130/
        cover:cover,    封面
        title:title,    标题
        }]
        """
        pass

    @abstractmethod
    def parseSearchResult(self, json):
        """
        解析json成app标准的数组
        如果search搜索结果可以满足需求的话，
        也可以不解析，函数原样返回json即可
        :param json: 使用search函数的搜索结果
        :return: app标准的数组 带*标为必有属性
        [{
        url:url,        *   整部动漫的url，如：http://susudm.com/acg/2130/
        cover:cover,    *   封面
        title:title,    *   标题
        latest:latest       最新集数（最新连载）
        area:area,          地区
        time:time,          时间
        stars:stars         演员
        }]
        就这7个部分
        """
        pass

    @abstractmethod
    def detail(self, func, url):
        """
        获取动漫的详情信息
        详情信息指总共多少集和每一集的播放地址
        :param url: 动漫的url 如：http://susudm.com/acg/2130/
        :param func: 打印日志函数
        :return: 详情信息
        {
            1: ['第1集'.'第1集的url'],   这里的 “第1集的url” 可以是存放url链接的json文件，也可以是真实的播放链接
            2: ['第2集'.'第2集的url']    根据接口而定
        }
        """
        pass

    @abstractmethod
    def getVideoUrl(self, url):
        """
        获取视频真实播放链接
        如果url已经是真实播放链接，将url原样返回即可
        :param url: 存放真实播放链接的json文件的url
        :return: 真实的播放链接
        """
        pass

    # @abstractmethod
    def getAllLinks(self, result, log):
        """
        获取动漫的全部链接
        :param result: 由detail()函数获取的结果 如： {1: ['第1集', 'url'], 2: ['第2集', 'url']}
        :param log: 打印日志函数
        :return: 不返回值，直接把链接保存到文本中
        """
        # 捕获异常
        try:
            log('正在抓取链接')
            log('【提示】在未出现成功提示之前最好不要离开此页面！')
            log('...')
            Num = len(result)
            # 格式化集数：第1集 --> 第01集 根据集数而定
            n = TextUtil.getIntegerDigits(Num)
            f = '第%0{}d集'.format(n)
            for i in range(1, Num + 1):
                name = result[i][0]
                if re.match('第(.*?)集', name):
                    num = re.findall('第(.*?)集', name)[0]
                    # 看下num是不是整数
                    if re.match(r'\d *', num):
                        name = f % int(num)
                        result.update({i: [name, result[i][1]]})
                pass

            # 创建文件
            desktop = TextUtil.get_desktop()
            file = open(desktop + '/download.txt', 'w')
            file.close()
            for i in range(1, Num + 1):
                time.sleep(1)
                # print(result[i][0])
                with open(desktop + '/download.txt', 'a') as f:
                    f.write(result[i][0] + '@' + self.getVideoUrl(result[i][1]) + '\n')
                    log('【{}】'.format(result[i][0]))
                    print('【{}】'.format(result[i][0]))
                    pass
                pass
            log('抓取完成！')
            log('以保存至 ' + desktop + '\\download.txt')
        except Exception as e:
            print('yc')
            print(e.args)
        pass

    pass
