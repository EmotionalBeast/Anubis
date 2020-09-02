# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/02 20:20

"""
方案：
1、多线程进行测试
2、封装locust进行压测： locust -f locutfile.py -u 1 -n 1 --run-time 30m --csv=./
"""

import json
from locust import HttpUser, task

dic = {
    "method": "",
    "host": "",
    "path": "",
    "params":{}
}

class Stress(HttpUser):
    def __init__(self):
        super(Stress, self).__init__()
        self.host = dic['host']

    @task
    def run(self):
        pass

class StressGet(Stress):
    
    @task
    def run(self):
        self.client.get(dic["path"], params=dic["params"])

class StressPost(Stress):

    @task
    def run(self):
        self.client.post(dic["path"], parms=dic["params"])
