#coding = utf-8

import math
import GetGitLog as gitLog

import os
import pandas as pd

def toDF(commitNumToDate:dict):
    df = {
        'time':commitNumToDate.keys(),
        'num':commitNumToDate.values()
    }
    data = pd.DataFrame(df)
    return data

def exportExcel(comToDate:dict):
    dir_path = os.path.dirname(os.path.abspath(__file__))#当前目录
    file_names = os.listdir(dir_path)
    all_data = pd.DataFrame()
    path = "res"
    if(not os.path.exists(path)):
        os.makedirs(path)
    resPathName = path + '/gitLogTime.xlsx'
    writer = pd.ExcelWriter(resPathName, engine='openpyxl')
    data = toDF(comToDate)
    file_name = "sheet1"
    print("file_name:" + file_name)
    data.to_excel(writer, sheet_name = file_name, index=False)
    writer.save()
    os.system("pause")

if __name__ == "__main__":
    logList = gitLog.transLogInfo()
    logList = gitLog.findLogsByName("c2909371614", logList)
    commitNumToDate = gitLog.findLogsByTimeZone(logList)
    print(commitNumToDate)
    importExcel(commitNumToDate)
    # data = toDF(commitNumToDate)
    # print(data)
    # hue = []
    # print(commitNumToDate.keys(), commitNumToDate.values())



            
