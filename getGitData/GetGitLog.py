#coding = utf-8

import subprocess
from datetime import datetime
from LogData import LogData
import re
import copy

def get_git_log():
    '''利用git命令获取log字符串'''
    # 使用 subprocess 运行 git log 命令，并捕获输出
    # result = subprocess.run("git log", text = True)
    # result = subprocess.Popen("git log", text = True)
    result = subprocess.check_output("git log", encoding="utf-8")
    return result

def getDateTimeByStr(str):
    '''转换日期'''
    # print("str:",str)
    str = str[:str.find("+")]
    time_obj = ""
    try:
        time_obj = datetime.strptime(str, "Date:   %a %b %d %H:%M:%S %Y ")
    except:
        time_obj = ""
    return time_obj

def getYMD_Time(time:datetime):
    '''只保留年月日'''
    return datetime(time.year, time.month, time.day)

def isSameDay(time_objA, time_objB):
    '''是否同一天'''
    if time_objA.year == time_objB.year and time_objA.month == time_objB.month and \
    time_objA.day == time_objB.day:
        return True
    return False

def delEmptyStr(strs = ["", "1", ""]):
    '''筛除字符串数组中的空字符串'''
    res = []
    for i in range(0, len(strs)):
        if (len(strs[i]) > 0):
            res.append(strs[i])
    return res 

def getLogDataByStrs(strs = ["", "1", "", ""]):
    '''获取字符串中的log信息'''
    res:list = []
    for i in range(0, len(strs), 4):
        # logData = LogData()
        # logData.commit_sha = (re.search(r'commit (\w+)', strs[i])).group(1)
        # authorStrs = strs[i+1].split(" ")
        # logData.author =  authorStrs[1]
        # logData.email = authorStrs[2]
        # logData.time = getDateTimeByStr(strs[i+2])
        # logData.log = strs[i+3].lstrip()

        if len(strs[i:i+4]) >= 4:
            logData = getLogData(strs[i:i+4])
            res.append(logData)
            # logData.printEle()#打印转换完的信息
    return res

def getLogData(ss:list):
    logData = LogData()
    for i in range(0, 4):
        match = re.search(r'^commit (\w+)', ss[i])
        if match:
            # print("ss:",ss[i])
            logData.commit_sha = match.group(1)
        elif ss[i].find("Author") != -1:
            authorStrs = ss[i].split(" ")
            logData.author =  authorStrs[1]
            logData.email = authorStrs[2]
        elif ss[i].find("Date") != -1:
            logData.time = getDateTimeByStr(ss[i])
        else:
            logData.log = ss[i].lstrip()
    return logData

def transLogInfo():
    '''获取日志并转换成特定数据'''
    log_info = get_git_log()
    logDataList = None
    if log_info is not None:
        # print(log_info)
        words = log_info.split("\n")
        wordsFilter = delEmptyStr(words)
        # print(wordsFilter, len(wordsFilter))
        logDataList = getLogDataByStrs(wordsFilter)
    return logDataList

def findLogsByName(name:str, logList):
    '''通过名字进行筛选，可以只输入部分名字'''
    res = []
    for i in range(0, len(logList)):
        author:str = logList[i].author
        if(author == name or author.find(name)):
            res.append(logList[i])
    return res

def findLogsByTimeZone(logList:list, limitStr = ["2022-08-30", "2099-08-30"]):
    '''限制搜索区间，获取commit次数'''
    # res = []
    dateFormat = "%Y-%m-%d"
    limitMax = datetime.strptime(limitStr[1], dateFormat)
    limitMin = datetime.strptime(limitStr[0], dateFormat)
    timeMax = copy.deepcopy(limitMin) #起始量 
    timeMin = copy.deepcopy(limitMax)
    commitNumToDate = {}
    for i in range(0, len(logList)):
        if logList[i].time == None:
            continue
        time:datetime = getYMD_Time(logList[i].time) 
        if time <= limitMax and time >= limitMin:
            timeStr:str = time.strftime(dateFormat)#索引
            value = commitNumToDate.get(timeStr)
            if value is None:
                commitNumToDate[timeStr] = 1
            else:
                commitNumToDate[timeStr] = value + 1
            #寻找区间
            if time > timeMax:
                timeMax = copy.deepcopy(time)
            if time < timeMin:
                timeMin = copy.deepcopy(time)
    commitNumToDate = dict(sorted(commitNumToDate.items()))
    return commitNumToDate

if __name__ == '__main__':
    logList = transLogInfo()
    logList = findLogsByName("c2909371614", logList)
    commitNumToDate = findLogsByTimeZone(logList)
    print(commitNumToDate)
    

    
