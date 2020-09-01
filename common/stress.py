# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 17:45

import threading
import locust

"""
方案：
1、多线程进行测试
2、封装locust进行压测： locust -f locutfile.py -c 1 -n 1
-c  --clients
-n  --num-request
"""

class StressRequest(object):
    #压力测试主体
    def __init__(self):
        self.request_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
  }
        self.request_url = ""
        self.request_parms = []
    

class DrawChart(object):
    def __init__(self):
        pass



