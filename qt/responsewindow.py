# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/01 11:29

import sys, json, os
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from qt.reponsewindowui import Ui_ResponseWindow

class ResponseWindow(QWidget, Ui_ResponseWindow):
    def __init__(self, response):
        super(ResponseWindow, self).__init__()
        self.setupUi(self)
        self.response = response
        self.showData()

    def showData(self):
        self.initTabWidget(self.response)
