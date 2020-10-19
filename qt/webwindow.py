# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/15 10:40

import sys, json, os, subprocess, time, signal
from threading import Thread
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QLabel, QGraphicsItem
from PyQt5.QtCore import QRect, Qt, QUrl
from qt.webwindowui import Ui_WebWindow

class WebWindow(QWidget, Ui_WebWindow):
    def __init__(self):
        super(WebWindow, self).__init__()
        self.setupUi(self)
        self.thread = Thread(target=self.start, args=())
        self.thread.start()
        time.sleep(1)
        self.browser.load(QUrl("http://localhost:8089"))
        
    def start(self):
        print(subprocess.call(["locust", "-f","./common/stress.py"]))

    def stop(self):
        pass
        
    
    
    
 



        
