'''
Created on Jan 20, 2020

@author: sk199
'''
import logging
from time import sleep

from labs.module01.SystemPerformanceAdaptor import SystemPerformanceAdaptor


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.info("Starting system performance app daemon thread...")

sysPerfAdaptor = SystemPerformanceAdaptor()
sysPerfAdaptor.daemon =True
sysPerfAdaptor.enableAdaptor = True
sysPerfAdaptor.start()

while (True):
    sleep(5)
    pass
