# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 16:12

import sys
from qt.mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
