# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/15 10:37


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Ui_WebWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 800)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.retranslateUi(Form)
           
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Locust Web"))