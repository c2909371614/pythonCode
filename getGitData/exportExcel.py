#coding = utf-8

import math
import GetGitLog as gitLog
import re
import os
import pandas as pd

def toDF(commitNumToDate:dict):
    df = {
        'time':commitNumToDate.keys(),
        'num':commitNumToDate.values()
    }
    data = pd.DataFrame(df)
    return data

def getExcelWriter(name:str):
    dir_path = os.path.dirname(os.path.abspath(__file__))#当前目录
    file_names = os.listdir(dir_path)
    all_data = pd.DataFrame()
    path = "res"
    if(not os.path.exists(path)):
        os.makedirs(path)
    resPathName = path + '/'+ name +'.xlsx'
    writer = pd.ExcelWriter(resPathName, engine='openpyxl')
    return writer

def exportExcel(comToDate:dict):
    '''单个sheet'''
    writer = getExcelWriter("gitLogTime")
    data = toDF(comToDate)
    file_name = "sheet1"
    print("file_name:" + file_name)
    data.to_excel(writer, sheet_name = file_name, index=False)
    writer.save()
    os.system("pause")

def getLegalNameStr(key:str):
    reg = r'\[.*?\]'
    temp = re.match(reg, key)
    name = re.sub(reg, "_", key)
    return name


def exportMultiSheet(logList:list):
    '''多个sheet, author作为sheet name'''
    writer = getExcelWriter("gitLogMulti")
    data_list = gitLog.getLogsDic(logList)
    # print("keys:", data_list.keys())
    for key in data_list.keys():
        comNumToDate = gitLog.findLogsByTimeZone(data_list[key])
        print(key, comNumToDate)
        data = toDF(comNumToDate)
        name = getLegalNameStr(key) 
        data.to_excel(writer, sheet_name = name, index=False)
    writer.save()
    # print(data_list)


if __name__ == "__main__":
    logList = gitLog.transLogInfo()
    exportMultiSheet(logList)
    # logList = gitLog.findLogsByName("c2909371614", logList)
    # commitNumToDate = gitLog.findLogsByTimeZone(logList)
    # print(commitNumToDate)
    # exportExcel(commitNumToDate)





            
