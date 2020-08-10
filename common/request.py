# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 16:17

import json, os, requests, random


class Request(object):

    def __init__(self, dic):
        self.dic = dic
    
    def switchMethod(self):
        if self.dic["method"] == "get":
            return self.get(self.dic["url"], self.dic["params"])
        if self.dic["method"] == "post":
            return self.post(self.dic["url"], self.dic["params"])

        
    def get(self, url, params):
        dic = {}
        response = requests.get(url, params=params, verify=False)
        dic["headers"] = {}
        dic["headers"] = response.headers
        

        dic["code"] = response.status_code
        try:
            dic['body'] = response.json()
        except Exception as e:
            print(e)
            dic['body'] = 'None'
        dic['text'] = response.text
        dic['time_consuming'] = response.elapsed.microseconds/1000
        dic['time_total'] = response.elapsed.total_seconds()

        return dic

    def post(self, url, params):
        dic = {}
        response = requests.post(url, data=params, verify=False)
        dic["code"] = response.status_code
        try:
            dic['body'] = response.json()
        except Exception as e:
            print(e)
            dic['body'] = 'None'
        dic['text'] = response.text
        dic['time_consuming'] = response.elapsed.microseconds/1000
        dic['time_total'] = response.elapsed.total_seconds()

        return dic

    
    def put(self, url, params, headers, file_param, file, f_type):
        pass
        

