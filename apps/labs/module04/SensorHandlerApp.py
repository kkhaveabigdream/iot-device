'''
Created on Feb 5, 2020

@author: sk199
'''
import logging
from time import sleep
from labs.module04.TempSensorAdaptorTask import TempSensorAdaptorTask

logging.getLogger().setLevel(logging.INFO)
#logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
logging.info("Starting temperature sensor adaptor  daemon thread...")


tempsensoradaptor = TempSensorAdaptorTask()
tempsensoradaptor.daemon = True
tempsensoradaptor.enableEmulator = True
tempsensoradaptor.start()

while (True):
    sleep(10)
    pass
    