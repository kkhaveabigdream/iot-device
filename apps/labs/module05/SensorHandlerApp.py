'''
Created on Feb 5, 2020 

@author: sk199
'''
import logging
from time import sleep
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor


logging.getLogger().setLevel(logging.INFO)
#logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
logging.info("Starting temperature sensor adaptor  daemon thread...")




multisensoradaptor = MultiSensorAdaptor()
multisensoradaptor.enableTempSensor        = True
multisensoradaptor.enableHumidSensor = True
multisensoradaptor.enableHI2CSensor      = True
MultiSensorAdaptor.start()


while (True):   
    sleep(10)
    pass
    