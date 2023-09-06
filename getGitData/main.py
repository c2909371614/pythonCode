# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.mainUI import Ui_MainWindow
import sys
# sys.path.append('..')  # 将上一级目录添加到模块搜索路径中
# import GetGitLog as gitLog
import GetGitLog as gitLog
import exportExcel as exExcel

    
def onClickExportExcel():
    print("click export")
    logList = gitLog.transLogInfo()
    exExcel.exportMultiSheet(logList)

def addEvent(ui:Ui_MainWindow):
    ui.pushButton.clicked.connect(onClickExportExcel)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    addEvent(ui)
    MainWindow.show()
    sys.exit(app.exec_())
