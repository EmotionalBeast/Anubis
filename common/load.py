# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/09/25 15:08


import json, os
from random import randint


FORMAT = ["jpg", "png", "JPG", "PNG", "jpeg", "JPEG"]
IMAGE_PATH = os.path.join(os.getcwd(), "pic")

class LoadHttp(object):

    def __init__(self, path):
        with open(path, "r") as f:
            content = f.read()
            self.http = json.loads(content)
            self.images = self.getImages()


    @property
    def data(self):
        return self.http["data"]

    @property
    def headers(self):
        return self.http["headers"]
    
    @property
    def host(self):
        return self.http["host"]
    
    @property
    def path(self):
        return self.http["path"]

    @property
    def method(self):
        return self.http["method"]

    @property
    def file_(self):
        return self.http["file"]

    
    def getImages(self):
        images = []
        for root, _, files in os.walk(IMAGE_PATH):
            for file_ in files:
                if file_.split(".") in FORMAT:
                    name = os.path.join(root, file_)
                    images.append(name)
        
        return images
    
    def getRandomImage(self):
        index = randint(0, len(self.images)-1)
        image = {'file': open('%s' % self.images[index], 'rb')}
        return image


    
    



