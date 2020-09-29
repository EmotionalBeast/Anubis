# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 16:13

from qt.mainwindowui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidget, QTabWidget
from PyQt5.QtCore import  Qt, QRect
from qt.handler import TreeWidgetHandler
from common.request import Request
from qt.responsewindow import ResponseWindow
from qt.webwindow import WebWindow

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
        if self.responseDic:
            self.responseWindow = ResponseWindow(self.responseDic)
            self.responseWindow.setWindowModality(Qt.ApplicationModal)
            self.responseWindow.show()
        else:
            pass

        

    def getData(self):
        self.requestDic["method"] = self.comboBox_1.currentText()
        self.requestDic["url"] = self.lineEdit.text()
        self.requestDic["params"] = {}
        for i in range(10):
            if self.tableWidget_2.item(i, 0).text() != "" and self.tableWidget_2.item(i, 1).text() != "":
                key = self.tableWidget_2.item(i, 0).text()
                value = self.tableWidget_2.item(i, 1).text()
                self.requestDic["params"][key] = value       
        self.requestDic["files"] = ""
        return self.requestDic

    def save(self):
        headers = {}
        data = {}
        url = self.lineEdit.text()
        for i in range(10):
            if self.tableWidget_1.item(i, 0).text() != "" and self.tableWidget_1.item(i, 1).text() != "":
                headers[self.tableWidget_1.item(i, 0).text()] = self.tableWidget_1.item(i, 1).text()
            if self.tableWidget_2.item(i, 0).text() != "" and self.tableWidget_2.item(i, 1).text() != "":
                data[self.tableWidget_2.item(i, 0).text()] = self.tableWidget_2.item(i, 1).text()
        


    
    def stressTest(self):
        self.web = WebWindow()
        self.web.setWindowModality(Qt.ApplicationModal)
        self.web.show()


        







    

        