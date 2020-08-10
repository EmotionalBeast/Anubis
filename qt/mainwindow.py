# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 16:13

from qt.mainwindowui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import  Qt
from qt.handler import TreeWidgetHandler
from common.request import Request

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.requestDic = {}

    
    def run(self):
        self.responseDic = Request(self.getData()).switchMethod()
        self.showResult()

    def initData(self):
        pass
    
    def showResult(self):
        self.label_4.setText("状态: %s, 耗时: %ss" %(self.responseDic["code"], self.responseDic["time_total"]))
        self.initHeadersTab(self.responseDic["headers"])
        

    def getData(self):
        self.requestDic["method"] = self.comboBox.currentText()
        self.requestDic["url"] = self.lineEdit.text()
        self.requestDic["params"] = {}
        for i in range(9):
            if self.tableWidget.item(i, 0).text() != "" and self.tableWidget.item(i, 1).text() != "":
                key = self.tableWidget.item(i, 0).text()
                value = self.tableWidget.item(i, 1).text()
                self.requestDic["params"][key] = value       
        self.requestDic["files"] = ""
        return self.requestDic
    


        







    

        