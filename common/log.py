# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 17:47

import logging, os, time
from logging.handlers import TimedRotatingFileHandler

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')

class LogHandler(logging.Logger):
    
    def __init__(self, file_name="sys.log", level=DEBUG):
        self.file = os.path.join(LOG_PATH, file_name)
        self.level = level
        self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        logging.Logger.__init__(self, self.name, level=level)
        self.__setFileHandler__()

    def __setFileHandler__(self):
        file_handler = TimedRotatingFileHandler(filename = self.file, when='D', interval=1, backupCount=15)
        file_handler.suffix = '%Y%m%d.log'
        file_handler.setLevel(self.level)
        file_handler.setFormatter(self.formatter)
        self.addHandler(file_handler)
