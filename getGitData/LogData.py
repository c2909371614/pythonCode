#coding = utf-8

from datetime import datetime


class LogData:
    commit_sha:str = None
    author:str = None
    email:str = None
    time:datetime = None
    log:str = ""
    

    def printEle(self):
        '''打印自身元素'''
        print("------logData-----")
        print("commit:%s \nauthor:%s \nemail:%s \ntime:%s \nlog:%s \n" \
              %(self.commit_sha, self.author, self.email, self.time.strftime("%Y-%m-%d"), self.log))

