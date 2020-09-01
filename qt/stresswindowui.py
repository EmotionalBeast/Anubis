# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/01 11:07


import json
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StressWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 900)
        Form.setFixedSize(1000, 900)
        
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 0, 100, 30))
        self.label_1.setText("用户数")

        self.spinBox_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_1.setGeometry(QtCore.QRect(150, 0, 50, 30))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 0, 100, 30))
        self.label_2.setText("每秒请求数")

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(360, 0, 50, 30))

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(420, 0, 60, 30))
        self.pushButton_1.setText("运行")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1000, 860))


        self.retranslateUi(Form)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "压力测试"))

