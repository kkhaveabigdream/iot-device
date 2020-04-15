'''
Created on Mar 11, 2020

@author: sk199
'''
import logging
from time import sleep
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.module06.TempSensorAdaptorTask import TempSensorAdaptorTask
from project.MultiSensorAdaptor import MultiSensorAdaptor

#from labs.common.SensorDataListener import SensorDataListener


logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.info("Starting temperature sensor adaptor daemon thread...")

multiSensorAdaptor = MultiSensorAdaptor()
multiSensorAdaptor.enableTempSensor=True
multiSensorAdaptor.enableHumidSensor = True
multiSensorAdaptor.run()


while (True):  
    sleep(10)
    pass
    
    