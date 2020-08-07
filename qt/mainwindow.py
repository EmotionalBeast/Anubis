# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 16:13

from abc import ABCMeta, abstractmethod

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr("_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
        