#coding = utf-8

import matplotlib.pyplot as plt
import math
import GetGitLog as gitLog
import matplotlib.font_manager as fm
from datetime import datetime, timedelta

def pltInit():
    # 加载字体文件
    font_path = fm.findfont("SimHei")
    # 设置字体  
    plt.rcParams["font.family"] = "SimHei"

def getYMD_ByZone(limitStr = ["2023-07-25", "2023-08-30"]):
    dateFormat = "%Y-%m-%d"
    limitMax = datetime.strptime(limitStr[1], dateFormat)
    limitMin = datetime.strptime(limitStr[0], dateFormat)
    time = limitMin
    res = []
    while time <= limitMax:
        timeStr = time.strftime(dateFormat)
        res.append(timeStr)
        # print(timeStr)
        time += timedelta(days=1)
    return res

def getDates_y(dates_x:list, comNumToDate:dict):
    res = []
    for i in range(0, len(dates_x)):
        item = 0
        if comNumToDate.get(dates_x[i]) == None:
            item = 0
        else:
            item = comNumToDate.get(dates_x[i])
        res.append(item)
    return res

def drawMultiPlot(logList:list, lineNum = 3, limitStr = ["2023-07-25", "2023-08-30"]):
    pltInit()
    data_list = gitLog.getLogsDic(logList)
    # print("keys:", data_list.keys())
    i = 0
    dates_x = getYMD_ByZone(limitStr)
    for key in data_list.keys():
        if i >= 3:
            break
        i += 1
        comNumToDate = gitLog.findLogsByTimeZone(data_list[key], limitStr)
        comNumToDate = dict(sorted(comNumToDate.items()))
        print(key, comNumToDate)
        plt.plot(dates_x, getDates_y(dates_x, comNumToDate), label = key)
    plt.legend(loc = "best")
    step = math.floor(len(dates_x) / 10)
    ticks = [dates_x[i] for i in range(0, len(dates_x), step)]
    # labels = ["2023-07-25", "2023-08-30"]
    plt.xticks(ticks, rotation = 45)
    plt.show()



if __name__ == "__main__":
    logList = gitLog.transLogInfo()
    drawMultiPlot(logList)
    # logList = gitLog.findLogsByName("c2909371614", logList)
    # commitNumToDate = gitLog.findLogsByTimeZone(logList)
    # nameDicList = gitLog.getLogsDic(logList)
    # print(nameDicList)
    # print(commitNumToDate)

    # hue = []
    # print(commitNumToDate.keys(), commitNumToDate.values())
    

    # plt.scatter(commitNumToDate.keys(), commitNumToDate.values(), label = "c")

    # f, ax1 = plt.subplots()
    # ax1.plot(commitNumToDate.keys(), commitNumToDate.values(), label = "")
    # ax1.plot(commitNumToDate.keys(), commitNumToDate.values(), label = "字典")
    # ax1.plot(commitNumToDate.keys(), [1] * len(commitNumToDate), label = "ao")
    # ax1.legend(loc='best')
    # ax1.set_title("绘制测试", fontproperties='SimHei')
    # plt.show()

            
