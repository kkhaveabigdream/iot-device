'''
Created on Feb 5, 2020

@author: sk199
'''
import logging
from time import sleep
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.info("Starting temperature emulator adaptor  daemon thread...")

tempsensoradaptor = TempSensorAdaptorTask()
tempsensoradaptor.daemon = True
tempsensoradaptor.enableEmulator = True
tempsensoradaptor.start()

while (True):
    sleep(10)
    pass
