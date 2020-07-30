# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 19:57

import os, json

class Config(object):
    def __init__(self, path):
        self.path = path
        self.content = self.getContent()

    def getContent(self):
        with open(self.path, "r") as f:
            tmp = f.read()
        return tmp

class ConfigJson(Config):

    @property
    def jsonDic(self):
        dic = {}
        dic = json.dumps(self.content, strict=False)
        return dic

