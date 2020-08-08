# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assert1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

COMBOX_ITEM_LIST = ["get", "post"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
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
        self.tableWidget.setGeometry(QtCore.QRect(400, 140, 590, 295))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(9)
        _translate = QtCore.QCoreApplication.translate
        for i in range(2):
            self.tableWidget.setColumnWidth(i, 286)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))

        for i in range(9):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem())

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 450, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 490, 60, 30))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 490, 200, 30))
        # self.label_4.setText("状态: %s, 耗时: %ss")
        self.label_4.setObjectName("label_4")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(400, 530, 590, 370))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "接口测试"))
        self.label.setText(_translate("MainWindow", "路径"))
        self.label_2.setText(_translate("MainWindow", "参数"))
        self.label_3.setText(_translate("MainWindow", "结果"))
        self.pushButton.setText(_translate("MainWindow", "运行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.actionNew.setText(_translate("MainWindow", "新建"))
        self.menuTools.setTitle(_translate("MainWindow", "工具"))
        self.actionStress.setText(_translate("MainWindow", "压力测试"))

    def initJsonTab(self, headers):
        #数据解析部分
        self.model = QtGui.QStandardItemModel(len(headers.keys()), 2)


        #UI显示部分
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableView = QtWidgets.QTableView(self.tab_1)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setShowGrid(False)
        self.tableView.setModel(self.model)
        
    def initImageTab(self):
        pass

    def initHeadersTab(self):
        pass

    def initTextTab(self):
        pass
    
    def initContentTab(self):
        pass

