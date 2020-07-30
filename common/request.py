# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 16:17

import json, os, requests, random


class Request(object):
    def __init__(self):
        pass

    def get(self, url, data, headers):
        dic = {}
        response = requests.get(url, data=data, headers=headers, verify=False)

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

    def post(self, url, data, headers):
        dic = {}
        response = requests.post(url, json=data, headers=headers, verify=False)
        dic["code"] = response.status_code
        try:
            dic['body'] = response.json()
        except Exception as e:
            dic['body'] = 'None'
        dic['text'] = response.text
        dic['time_consuming'] = response.elapsed.microseconds/1000
        dic['time_total'] = response.elapsed.total_seconds()

        return dic

    def put(self, url, data, headers, file_param, file, f_type):
        pass
        

