# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.mainUI import Ui_MainWindow
import sys
import GetGitLog as gitLog
import exportExcel as exExcel
import drawGit

class Util:

    logList = None

    def onClickExportExcel(self):
        print("click export")
        if self.logList == None:
            self.logList = gitLog.transLogInfo()
        exExcel.exportMultiSheet(logList)

    def onClickDraw(self):
        print("click draw")
        if self.logList == None:
            self.logList = gitLog.transLogInfo()
        drawGit.drawMultiPlot(logList)

    def addEvent(self, ui:Ui_MainWindow):
        ui.pushButton.clicked.connect(self.onClickExportExcel)
        ui.pushButton_2.clicked.connect(self.onClickDraw)

    def updateListWidet(self, ui:Ui_MainWindow, names:list):
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
    util = Util()
    util.addEvent(ui)
    util.updateListWidet(ui, list(data_list.keys()))
    
    MainWindow.show()
    sys.exit(app.exec_())
