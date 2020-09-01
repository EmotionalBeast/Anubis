# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/01 11:16

import json
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResponseWindow(object):
    def setupUi(self, Form):
        self.index = 0

        Form.setObjectName("Form")
        Form.resize(600, 800)
        Form.setFixedSize(600, 800)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 30))
        self.label.setObjectName("label")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 600, 760))
        self.tabWidget.setObjectName("tabWidget")

        self.retranslateUi(Form)
           
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "响应内容"))

    
    def initJsonTab(self, dic):
        #数据解析部分
        # jsonStr = str(dic)
        jsonStr = json.dumps(dic, sort_keys=True, indent=2, ensure_ascii=False)

        #UI显示部分
        self.tab_2 = QtWidgets.QTableView()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 600, 760))
        self.textBrowser.setVerticalScrollBarPolicy(True)
        self.textBrowser.setPlainText(jsonStr)
        self.tabWidget.addTab(self.tab_2, "Json")

        
    def initImageTab(self):
        pass

    def initHeadersTab(self, headers):
        #数据解析部分
        keys = list(headers.keys())
        row = len(keys)
        self.model = QtGui.QStandardItemModel(row, 2)
        for i in range(row):
            name = QtGui.QStandardItem(keys[i])
            value = QtGui.QStandardItem(headers[keys[i]])
            self.model.setItem(i, 0, name)
            self.model.setItem(i, 1, value)
        #UI显示部分
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableView = QtWidgets.QTableView(self.tab_1)
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.model) 
        self.tableView.setGeometry(QtCore.QRect(0, 0, 600, 760))        
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setShowGrid(False)              
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tabWidget.addTab(self.tab_1, "Header")

    def initTextTab(self):
        pass
    
    def initContentTab(self):
        pass

    def initTabWidget(self, response):
        if self.index > 0:
            self.tabWidget.close()
            self.tabWidget = QtWidgets.QTabWidget()
            self.tabWidget.setGeometry(QtCore.QRect(0, 40, 600, 760))
            self.tabWidget.setObjectName("tabWidget")
        self.label.setText("状态: %s, 耗时: %ss" %(response["code"], response["time_total"]))
        self.initHeadersTab(response["headers"])
        if response["type"].split(";")[0] == "application/json":
            self.initJsonTab(response["body"])       
        # if self.response["type"].split("/")[0] == "image":
        #     self.initImageTab(response["type"]) ==
        
        # if self.response[""]
        
        self.index += 1
        self.tabWidget.show()


