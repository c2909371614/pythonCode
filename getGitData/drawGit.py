#coding = utf-8

import matplotlib.pyplot as plt
import math
import GetGitLog as gitLog

logList = gitLog.transLogInfo()
logList = gitLog.findLogsByName("c2909371614", logList)
commitNumToDate = gitLog.findLogsByTimeZone(logList)
print(commitNumToDate)

# hue = []
print(commitNumToDate.keys(), commitNumToDate.values())
plt.scatter(commitNumToDate.keys(), commitNumToDate.values())
plt.show()

            
