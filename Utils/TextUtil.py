"""
执行文本（字符串）的操作
"""
import winreg

from PyQt5.QtCore import QDateTime


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]


def getIntegerDigits(num):
    """
    获取整数的位数
    :param num: 整数
    :return: 位数
    """
    t = 1
    k = 10
    while True:
        if num < k:
            return t
        else:
            t += 1
            k *= 10
    pass


def getHelloWord(datetime: QDateTime):
    """
    根据当前时间返回 上午好/中午好/下午好
    :param datetime: 时间
    :return: list ['早上', '早上好', '今天要来点什么呢？\n我这里什么都有哦!']
    """
    hello = ['', '你好', '看点什么吧！\n什么都行哦！']
    hour = int(datetime.currentDateTime().toString("hh"))
    if 23 <= hour or hour < 2:
        hello = ['午夜', '还没睡呢', '你是否在思考问题呢，\n不妨跟我一起来放松一下！']
    elif 2 <= hour < 5:
        hello = ['凌晨', '快睡觉吧', '明天还有工作呢！\n真的真的不能熬夜的！']
    elif 5 <= hour < 7:
        hello = ['清晨', '起好早啊', '莫非是通宵了？\n这可不是好习惯呀！']
    elif 7 <= hour < 8:
        hello = ['早上', '早上好', '今天要来点什么呢？\n我这里什么都有哦！']
    elif 8 <= hour < 11:
        hello = ['上午', '上午好', '今天想要看点什么呢？\n我这里什么都有哦！(大概)']
    elif 11 <= hour < 13:
        hello = ['中午', '中午好', '今天想要看点什么呢？\n我这里什么都有哦！(大概)']
    elif 13 <= hour < 17:
        hello = ['下午', '下午好', '今天想要看点什么呢？\n我这里什么都有哦！(大概)']
    elif 17 <= hour < 19:
        hello = ['傍晚', '下班了', '是要先吃饭呢，\n还是先欣赏我呢？']
    elif 19 <= hour < 22:
        hello = ['晚上', '晚上好', '好好放松一下吧，\n我这里有好看的哦！']
    elif 22 <= hour < 23:
        hello = ['深夜', '夜深了', '早点休息吧！\n不要依依不舍了！']
    return hello
    pass
