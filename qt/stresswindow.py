# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/01 17:26


import sys, json, os
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect, Qt
from qt.stresswindowui import Ui_StressWindow


class StressWindow(QWidget, Ui_StressWindow):

    def __init__(self):
        super(StressWindow, self).__init__()
        self.setupUi(self)
