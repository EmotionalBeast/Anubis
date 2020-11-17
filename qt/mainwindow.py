# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 16:13

import os, json, re, shutil
from qt.mainwindowui import Ui_MainWindow
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QTableWidget, 
                        QTabWidget, QTreeWidgetItem, QMenu, QAction, QTableWidgetItem, QMessageBox)
from PyQt5.QtCore import  Qt, QRect
from PyQt5.QtGui import QCursor
from qt.handler import TreeWidgetHandler
from common.request import Request
from qt.responsewindow import ResponseWindow
from qt.webwindow import WebWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.requestDic = {}
        self.initTree()

    
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
        #保存请求的信息
        request = {}
        headers = {}
        data = {}
        url = self.lineEdit.text()
        method = self.comboBox_1.currentText()
        for i in range(10):
            if self.tableWidget_1.item(i, 0).text() != "" and self.tableWidget_1.item(i, 1).text() != "":
                headers[self.tableWidget_1.item(i, 0).text()] = self.tableWidget_1.item(i, 1).text()
            if self.tableWidget_2.item(i, 0).text() != "" and self.tableWidget_2.item(i, 1).text() != "":
                data[self.tableWidget_2.item(i, 0).text()] = self.tableWidget_2.item(i, 1).text()
        hosts = re.findall(r"(http://|https://)?([^/]*)", url)[0]
        host = hosts[0] + hosts[1] 
        print(host)
        path = url.replace(host, "")
        request["headers"] = headers
        request["data"] = data
        request["method"] = method
        request["host"] = host
        request["path"] = path
        # request["file"] = False

        # with open("./path", "w") as f:
        #     jsonStr = json.dumps(request, sort_keys=True, indent=2, ensure_ascii=False)
        #     f.write(jsonStr)
        
        with open("./common/stress.json", "w") as f:
            jsonStr = json.dumps(request, sort_keys=True, indent=2, ensure_ascii=False)
            f.write(jsonStr)
                  
    def stressTest(self):
        self.save()
        self.web = WebWindow()
        self.web.setWindowModality(Qt.ApplicationModal)
        self.web.show()
    
    ###################################################################################################
    #treeWidget
    def getTreeDic(self):
        #获取文件夹结构
        tree = {}
        for root, dirs, files in os.walk("./case"):
            for dir in dirs:
                tree[dir] = []
            for file in files:
                dirName = root.split("/")[-1]
                if dirName in tree.keys():
                    tree[dirName].append(file)
        return tree

    def initTree(self):
        #展示文件夹结构
        tree = self.getTreeDic()
        for key in tree.keys():
            root = QTreeWidgetItem(self.treeWidget)
            root.setText(0, key)
            for value in tree[key]:
                name = value.split(".")[0]
                child = QTreeWidgetItem()
                child.setText(0, name)
                root.addChild(child)
    
    def treeRightButtonFunc(self):
        item = self.treeWidget.currentItem()
        if item != None:
            if item.parent() != None:
                menu = QMenu()
                menu.addAction(QAction("增加用例", self))
                menu.addAction(QAction("删除用例", self))
                menu.addAction(QAction("重命名", self))
                menu.triggered[QAction].connect(self.caseProcessTrigger)
                menu.exec_(QCursor.pos())
            else:
                menu = QMenu()
                menu.addAction(QAction("新建项目", self))
                menu.addAction(QAction("删除项目", self))
                menu.addAction(QAction("重命名", self))
                menu.triggered[QAction].connect(self.projectProcessTrigger)
                menu.exec_(QCursor.pos())
        else:
            menu = QMenu()
            menu.addAction(QAction("新建项目", self))
            menu.triggered[QAction].connect(self.projectProcessTrigger)
            menu.exec_(QCursor.pos())
                
    
    def caseProcessTrigger(self, item):
        if item.text() == "增加用例":
            self.caseAdd()
        
        if item.text() == "删除用例":
            self.caseDel()

        if item.text() == "重命名":
            self.caseRename()
    
    def caseDel(self):
        item = self.treeWidget.currentItem()
        parentItem = self.treeWidget.currentItem().parent()
        path = "./case/" + parentItem.text(0) + "/" + item.text(0) + ".json"
        if os.path.exists(path):
            os.remove(path)
            parentItem.removeChild(item)
            

    def caseAdd(self): 
        #先增加节点，再处理文件
        parentItem = self.treeWidget.currentItem().parent()
        child = QTreeWidgetItem()
        parentItem.addChild(child)
        # self.treeWidget.setCurrentItem(parentItem.child(parentItem.childCount()-1))
        self.treeWidget.setCurrentItem(child)
        item = self.treeWidget.currentItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.treeWidget.editItem(item)
        self.treeWidget.itemChanged.connect(lambda: self.caseAddHandler(item, parentItem))
    
    def caseAddHandler(self, item, parentItem):
        pathNew = "./case/" + parentItem.text(0) + "/" + item.text(0) + ".json"
        if os.path.exists(pathNew):
            QMessageBox.information(self, "提示", "名称已存在！请重新取名!")
            self.treeWidget.itemChanged.disconnect()
            item.setText(0, "未命名")
            path = "./case/" + parentItem.text(0) + "/" + item.text(0) + ".json"
            content =  {"data":{}, "headers":{}, "host":"", "method":"", "path":""}
            with open(path, "w") as f:
                text = json.dumps(content, sort_keys=True, indent=2, ensure_ascii=False)
                f.write(text)
        else:
            self.treeWidget.itemChanged.disconnect()
            content =  {"data":{}, "headers":{}, "host":"", "method":"", "path":""}
            with open(pathNew, "w") as f:
                text = json.dumps(content, sort_keys=True, indent=2, ensure_ascii=False)
                f.write(text)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        
    
    def caseRename(self):
        item = self.treeWidget.currentItem()
        parentItem = self.treeWidget.currentItem().parent()
        oldName = item.text(0)
        pathOld = "./case/" + parentItem.text(0) + "/" + item.text(0) + ".json"
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.treeWidget.editItem(item)
        self.treeWidget.itemChanged.connect(lambda: self.caseRenameHandler(item, parentItem, oldName, pathOld))
        
    
    def caseRenameHandler(self, item, parentItem, oldName, pathOld):
        pathNew = "./case/" + parentItem.text(0) + "/" + item.text(0) + ".json"
        if os.path.exists(pathNew):
            QMessageBox.information(self, "提示", "名称已存在！请重新取名!")
            self.treeWidget.itemChanged.disconnect()
            item.setText(0, oldName)
        else:
            self.treeWidget.itemChanged.disconnect()
            os.rename(pathOld, pathNew)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

    #project
    def projectProcessTrigger(self, item):
        if item.text() == "新建项目":
            self.projectAdd()

        if item.text() == "删除项目":
            self.projectDel()
        
        if item.text() == "重命名":
            self.projectRename()
            

    def projectDel(self):
        item = self.treeWidget.currentItem()
        path = "./case/" + item.text(0)
        if os.path.exists(path):
            shutil.rmtree(path)
            self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item))

    
    def projectAdd(self):
        root = QTreeWidgetItem(self.treeWidget)
        child = QTreeWidgetItem()
        child.setText(0, "未命名")
        root.addChild(child)
        self.treeWidget.setCurrentItem(root)
        item = self.treeWidget.currentItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.treeWidget.editItem(item)
        self.treeWidget.itemChanged.connect(lambda: self.projectAddHandler(item))
    
    def projectAddHandler(self, item):
        path = "./case/" + item.text(0)
        if os.path.exists(path):
            path1 = "./case/未命名"
            os.mkdir(path1)
            pathFile = path1 + "/未命名.json"
            content =  {"data":{}, "headers":{}, "host":"", "method":"", "path":""}
            with open(pathFile, "w") as f:
                text = json.dumps(content, sort_keys=True, indent=2, ensure_ascii=False)
                f.write(text)
            self.treeWidget.itemChanged.disconnect()
            item.setText(0, "未命名")
        else:
            self.treeWidget.itemChanged.disconnect()
            os.mkdir(path)
            pathFile = path + "/未命名.json"
            content =  {"data":{}, "headers":{}, "host":"", "method":"", "path":""}
            with open(pathFile, "w") as f:
                text = json.dumps(content, sort_keys=True, indent=2, ensure_ascii=False)
                f.write(text)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        

    def projectRename(self):
        item = self.treeWidget.currentItem()
        oldName = item.text(0)
        pathOld = "./case/" + item.text(0)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.treeWidget.editItem(item)
        self.treeWidget.itemChanged.connect(lambda: self.projectRenameHandler(item, oldName, pathOld))
    
    def projectRenameHandler(self, item, oldName, pathOld):
        pathNew = "./case/" + item.text(0)
        if os.path.exists(pathNew):
            QMessageBox.information(self, "提示", "名称已存在！请重新取名!")
            self.treeWidget.itemChanged.disconnect()
            item.setText(0, oldName)
        else:
            self.treeWidget.itemChanged.disconnect()
            os.rename(pathOld, pathNew)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

    #############################################################################################################
        
    
    def childItemClick(self, item, column):
        if item.parent() != None:
            path = "./case/" + item.parent().text(0) + "/" + item.text(0) + ".json"
            self.loadJsonData(path)
    
    def loadJsonData(self, path):
        with open(path, "r") as f:
            jsonStr = f.read()
            dic = json.loads(jsonStr, strict = False)
        self.initTable()
        self.comboBox_1.setCurrentText(dic["method"])
        self.lineEdit.setText(dic["host"] + dic["path"])
        headerKeys = list(dic["headers"].keys())
        headerValues = list(dic["headers"].values())
        for i in range(len(headerKeys)):
            self.tableWidget_1.setItem(i,0, QTableWidgetItem(headerKeys[i]))
            self.tableWidget_1.setItem(i,1, QTableWidgetItem(str(headerValues[i])))

        dataKeys = list(dic["data"].keys())
        dataValues = list(dic["data"].values())
        for i in range(len(dataKeys)):
            self.tableWidget_2.setItem(i,0, QTableWidgetItem(dataKeys[i]))
            self.tableWidget_2.setItem(i,1, QTableWidgetItem(str(dataValues[i])))

    

        
    
        


        







    

        