# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/30 13:29

import logging

if __name__ == "__main__":
    print(logging.NOTSET)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    logging.warning('this is warning')
    logging.info('this is info')

    logger = logging.getLogger('apps')
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    apps_handler = logging.FileHandler(filename="apps.log")
    apps_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    apps_handler.setFormatter(apps_formatter)
    logger.addHandler(apps_handler) 
    logger.debug('shit')

    child_logger = logging.getLogger('apps.f')
    child_logger.info('haha')
