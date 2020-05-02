class string:
    NONE = ''

    APP_NAME = '看番神器 Pro'

    VERSION = 'V1.2.0 正式版'

    OPEN_SOURCE = 'https://github.com/Tanyiqu/AnimeArtifactPro'

    WELCOME = """
欢迎使用【%s】
此软件完全免费！并且项目开源！
另外只建议用此工具观看哔哩哔哩没有的番剧，因为有弹幕看的才有意思。
由于目标网站也是使用爬虫进行资源收集的，所以不保证视频的清晰度！大部分的视频清晰度都是很给力的，甚至有1080+的。
个人认为，就算有清晰度极差的视频，只要下载到手机上（虽然有些下载不了），观看观感不会影响太多。
""" % APP_NAME

    # M3U8_API = 'https://www.m3u8play.com/?play='
    M3U8_API = 'https://www.nxflv.com/?url='

    TUTORIAL = 'https://www.bilibili.com/video/BV1Gp4y1y74c'

    DOWNLOAD_LINK = 'https://tanyiqu.lanzous.com/b0cq4peeb'

    UPDATE_LOG = [
        {
            'version': 'V1.2.0 正式版',
            'time': '2020.04.27',
            'downloadNum': 0,
            'detail': [
                '1.添加备用播放器功能、解析m3u8视频（网速不快的话，体验应该会不佳）',
                '2.更改主界面比例为16:9,',
                '3.添加播放下一集功能',
                '4.新增接口2（太垃圾了，这个网站！实在没有好网站让我做测试><）',
                '5.提供临时更换背景图的解决方案，详情在“使用教程”分集里面',
                '...'
            ]
        },
        {
            'version': 'V1.2.0',
            'time': '2020.0',
            'downloadNum': 0,
            'detail': [
                '1.添加接口3',
                '2.对所有接口添加抓取链接功能',
                '...'
            ]
        },
        {
            'version': 'V1.1.0 正式版',
            'time': '2020.04.20',
            'downloadNum': 489,
            'detail': [
                '1.添加设置功能',
                '2.添加批量下载功能',
                '3.添加检查更新功能',
                '...'
            ]
        },
        {
            'version': 'V1.0.1 测试版',
            'time': '2020.04.19',
            'downloadNum': 170,
            'detail': [
                '1.添加使用教程的接口',
                '2.添加更新日志',
                '3.修复“关于按钮”的一些bug',
                '4.优化开启App时的流畅度',
                '...'
            ]
        },
        {
            'version': 'V1.0 测试版',
            'time': '2020.04.12',
            'downloadNum': 186,
            'detail': [
                '1.发布',
                '...'
            ]
        }
    ]
