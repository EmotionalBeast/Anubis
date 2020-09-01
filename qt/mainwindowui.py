# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assert1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import json
from PyQt5 import QtCore, QtGui, QtWidgets

COMBOX_ITEM_LIST = ["get", "post"]

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

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 40, 100, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(COMBOX_ITEM_LIST)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 45, 460, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 100, 60, 30))
        self.label_2.setObjectName("label_2")

        

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(400, 140, 590, 600))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(19)
        _translate = QtCore.QCoreApplication.translate
        for i in range(2):
            self.tableWidget.setColumnWidth(i, 283)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))

        for i in range(19):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem())

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 750, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(870, 750, 100, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.save)
 

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 390, 900))
        self.treeWidget.setObjectName("treeWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderLabels(["测试集"])

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

        self.actionStress = QtWidgets.QAction(MainWindow)
        self.actionStress.setObjectName("actionStress")
        self.menuFile.addAction(self.actionNew)
        self.menuTools.addAction(self.actionStress)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.actionStress.triggered.connect(self.showStressWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "接口测试"))
        self.label.setText(_translate("MainWindow", "路径"))
        self.label_2.setText(_translate("MainWindow", "参数"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton.setText(_translate("MainWindow", "保存"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.menuTools.setTitle(_translate("MainWindow", "工具"))
        self.actionStress.setText(_translate("MainWindow", "压力测试"))
        self.actionStress.setShortcut(_translate("MainWindow", "Ctrl+Q"))


        
        

