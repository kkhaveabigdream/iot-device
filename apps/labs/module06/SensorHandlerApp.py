'''
Created on Feb 5, 2020 

@author: sk199
'''
import logging
from time import sleep
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.module06.TempSensorAdaptorTask import TempSensorAdaptorTask

#from labs.common.SensorDataListener import SensorDataListener


logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.info("Starting temperature sensor adaptor daemon thread...")

mqttClient = MqttClientConnector()
mqttClient.run()


while (True):  
    sleep(10)
    pass
    