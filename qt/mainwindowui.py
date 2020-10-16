# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assert1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import json
from PyQt5 import QtCore, QtGui, QtWidgets

METHOD = ["get", "post"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.index = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        MainWindow.setFixedSize(1000, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 0, 60, 30))
        self.label.setObjectName("label")

        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(400, 40, 100, 30))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItems(METHOD)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 45, 460, 20))
        self.lineEdit.setObjectName("lineEdit")

        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(400, 140, 590, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.headersTableInit()
        self.dataTableInit()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 750, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run)

        # self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_1.setGeometry(QtCore.QRect(870, 750, 100, 30))
        # self.pushButton_1.setObjectName("pushButton_1")
        # self.pushButton_1.clicked.connect(self.save)
 

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 390, 900))
        self.treeWidget.setObjectName("treeWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderLabels(["测试集"])
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.treeRightButtonFunc)
        self.treeWidget.itemClicked.connect(self.childItemClick)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)

        self.actionSend = QtWidgets.QAction(MainWindow)
        self.actionSend.setObjectName("actionSend")
        self.menuTools.addAction(self.actionSend)


        self.actionStress = QtWidgets.QAction(MainWindow)
        self.actionStress.setObjectName("actionStress")
        self.menuTools.addAction(self.actionStress)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.actionStress.triggered.connect(self.stressTest)
        self.actionSave.triggered.connect(self.save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "接口测试"))
        self.label.setText(_translate("MainWindow", "路径"))
        # self.label_2.setText(_translate("MainWindow", "参数"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        # self.pushButton_1.setText(_translate("MainWindow", "保存"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuTools.setTitle(_translate("MainWindow", "工具"))
        self.actionSend.setText(_translate("MainWindow", "发送请求"))
        self.actionSend.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionStress.setText(_translate("MainWindow", "压力测试"))
        self.actionStress.setShortcut(_translate("MainWindow", "Ctrl+P"))
    
    def headersTableInit(self):
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 0, 590, 351))
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(2)
        self.tableWidget_1.setRowCount(10)

        _translate = QtCore.QCoreApplication.translate
        for i in range(2):
            self.tableWidget_1.setColumnWidth(i, 283)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_1.setHorizontalHeaderItem(i, item)
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))

        for i in range(10):
            self.tableWidget_1.setItem(i, 0, QtWidgets.QTableWidgetItem())
            self.tableWidget_1.setItem(i, 1, QtWidgets.QTableWidgetItem())
        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "头信息"))



    def dataTableInit(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 590, 351))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(10)

        _translate = QtCore.QCoreApplication.translate
        for i in range(2):
            self.tableWidget_2.setColumnWidth(i, 283)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(i, item)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))

        for i in range(10):
            self.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem())
            self.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem())
        self.tabWidget.addTab(self.tab_2, "")

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "参数"))
    
    def initTable(self):
        if self.index > 0:
            self.tabWidget.close()
            self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
            self.tabWidget.setGeometry(QtCore.QRect(400, 140, 590, 351))
            self.tabWidget.setObjectName("tabWidget")
            self.headersTableInit()
            self.dataTableInit()
            self.tabWidget.show()
        self.index += 1
        


    
    

        
        

