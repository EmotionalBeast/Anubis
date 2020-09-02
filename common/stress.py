# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 17:45


"""
方案：
1、多线程进行测试
2、封装locust进行压测： locust -f locutfile.py -u 1 -n 1 --run-time 30m --csv=./
"""
import json
from locust import HttpUser, task

class Stress(HttpUser):
    def __init__(self):
        super(Stress, self).__init__()
        self.request = RequestDic(dic)
        self.host = ""

    @task
    def run(self):
        pass

class StressGet(Stress):
    
    @task
    def run(self):
        self.client.get(self.request.path, params=self.request.params)

class StressPost(Stress):

    @task
    def run(self):
        self.client.post(self.request.path, parms=self.request.params)


class RequestDic(object):

    def __init__(self, dic):
        self.method = dic["method"]
        self.host = dic["host"]
        self.path = dic["path"]
        self.params = dic["params"]




    




