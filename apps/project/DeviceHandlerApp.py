'''
Created on Mar 11, 2020

@author: sk199
'''
import logging
from time import sleep
from project.MultiSensorAdaptor import MultiSensorAdaptor

#from labs.common.SensorDataListener import SensorDataListener


logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.info("Starting temperature sensor adaptor daemon thread...")

multiSensorAdaptor = MultiSensorAdaptor()
multiSensorAdaptor.enableTempSensor=True
multiSensorAdaptor.enableHumidSensor = True
multiSensorAdaptor.enableMoistureSensor = False
multiSensorAdaptor.run()


while (True):  
    sleep(10)
    pass
    
    