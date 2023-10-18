# -*- coding: utf-8 -*-
import PyPDF2
import re  

def getPosStr(str:str, pattern):
    matches = re.finditer(pattern, str)
    ids = [match.start() for match in matches]
    return ids
def removeErrorPos(pos1:list, pos2:list):
    for i in range(len(pos2)):
        if(pos2[i] - pos1[i] >= 100):
            pos1.remove(pos1[i])
            return pos1

def analysis():
    pathName = 'PDF_Analysis/塔罗全书'
    txtStr = ""
    with open(pathName + ".txt","r") as file:
        for line in file.readlines():
            txtStr += line
    # print(txtStr[:100])
    # txtStr.find("代表的谶")
    pattern = r'代表的谶(.*)大阿卡纳诸神解谶'
    pattern1 = r'代表的谶'
    pattern2 = r'大阿卡纳诸神解谶'
    pos1 = getPosStr(txtStr, pattern1)
    pos2 = getPosStr(txtStr, pattern2)
    pos1 = removeErrorPos(pos1, pos2)
    for i in range(len(pos1)):
        if(pos2[i] - pos1[i] <= 100):
            print(txtStr[pos1[i]:pos2[i]])
    

if __name__ == "__main__":
    print("main")
    analysis()
    
