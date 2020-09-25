# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 17:45


"""
方案：
1、多线程进行测试
2、封装locust进行压测： locust -f locutfile.py
"""

import json
from locust import HttpUser, task, between
from common.load import LoadHttp

HTTP = LoadHttp("./stress.json")

class Stress(HttpUser):
    wait_time = between(0.5, 1.5)
    host = HTTP.host

    def __init__(self):
        super(Stress, self).__init__()
        self.path = HTTP.path
        self.headers = HTTP.headers
        self.data = HTTP.data
    
    def get(self):
        self.client.get(self.path, headers=self.headers, params=self.data)

    def post(self):
        self.client.post(self.path, headers=self.headers, data=self.data)
    
    def post_with_file(self):
        self.client.post(self.path, headers=self.headers, data=self.data, files=HTTP.getRandomImage())

    @task
    def run(self):
        if HTTP.method == "get":
            self.get()
        elif HTTP.method == "post":
            if HTTP.file_:
                self.post_with_file()
            else:
                self.post()
    


    




