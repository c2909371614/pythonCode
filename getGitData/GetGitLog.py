#coding = utf-8

import subprocess
from datetime import datetime

def get_git_log():
    # 使用 subprocess 运行 git log 命令，并捕获输出
    # result = subprocess.run("git log", text = True)
    # result = subprocess.Popen("git log", text = True)
    result = subprocess.check_output("git log", encoding="utf-8")
    return result

def getDateTimeByStr(str):
    time_obj = datetime.strptime(str, "Date: %a %b %d %H:%M:%S %Y")
    return time_obj


def isSameDay(time_objA, time_objB):
    '''是否同一天'''
    if time_objA.year == time_objB.year and time_objA.month == time_objB.month and \
    time_objA.day == time_objB.day:
        return True
    return False


if __name__ == '__main__':
    log_info = get_git_log()
    if log_info is not None:
        print(log_info)