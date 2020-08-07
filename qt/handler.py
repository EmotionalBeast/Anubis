# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/08/07 19:57

from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import Qt

class TreeWidgetHandler(object):

    def __init__(self, treeWidget):
        self.treeWidget = treeWidget

    #右键添加子节点
    def addChildItem(self, root):
        pass
    
    #右键添加父节点
    def addRootItem(self, name):
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(name)
        root.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)

    #右键新增子节点
    def deleteChildItem(self, root):
        pass
    
    #右键根节点
    def deleteRootItem(self):
        pass


    #右键删除子节点
    def showItem(self):
        pass
    
    #子节点的选中操作
    def checkItem(self):
        pass




