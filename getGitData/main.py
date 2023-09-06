# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.mainUI import Ui_MainWindow
import sys
import GetGitLog as gitLog
import exportExcel as exExcel
import drawGit

logList = None

def onClickExportExcel():
    print("click export")
    if logList == None:
        logList = gitLog.transLogInfo()
    exExcel.exportMultiSheet(logList)

def onClickDraw():
    print("click draw")
    if logList == None:
        logList = gitLog.transLogInfo()
    drawGit.drawMultiPlot(logList)

def addEvent(ui:Ui_MainWindow):
    ui.pushButton.clicked.connect(onClickExportExcel)
    ui.pushButton_2.clicked.connect(onClickDraw)

def updateListWidet(ui:Ui_MainWindow, names:list):
    # names = ["ab", "bc", "de"]
    for i in range(0, len(names)):
        ui.listWidget.insertItem(i, names[i])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    logList = gitLog.transLogInfo()
    data_list = gitLog.getLogsDic(logList)#名字分组
    addEvent(ui)
    updateListWidet(ui, list(data_list.keys()))
    
    MainWindow.show()
    sys.exit(app.exec_())
