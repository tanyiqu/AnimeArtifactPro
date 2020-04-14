"""
执行文本（字符串）的操作
"""
import winreg


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
