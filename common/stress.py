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

class Stress(object):
    #压力测试
    def __init__(self):
        pass



