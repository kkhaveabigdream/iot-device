'''
Created on Feb 26, 2020

@author: sk199
'''
import paho.mqtt.client as mqtt
from labs.module06.TempSensorAdaptorTask import TempSensorAdaptorTask
import time
from labs.common.DataUtil import DataUtil
from labs.common.SensorData import SensorData
import logging


class MqttClientConnector(object):
    '''
    classdocs
    '''
    tempSensor = TempSensorAdaptorTask()
    sensorData = SensorData()
    dataUtil = DataUtil()
    client = mqtt.Client()

    def __init__(self):
        '''
        Constructor
        '''      

    '''
    Callback function
    '''
    
    def _on_connect(self,client,userdata,flags,rc):
        print("Connected with result code " + str(rc))
    
    def _on_disconnect(self,client,userdata,rc):
        print("Dissconnected with result code: " + str(rc))
                
    def _on_message(self,client,userdata,msg):
        print(msg.topic+"" + str(msg.payload))
        
    def getSensorData(self):
        temp = self.tempSensor.getTemperature()
        self.sensorData.addValue(temp)
        jsonData = self.dataUtil.toJsonFromSensorData(self.sensorData)
        return jsonData
    
    '''
    Connect to remote mqtt broker:mqtt.eclipse.org
    publish msg
    '''
   
    def run(self):
         
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self.client.connect("mqtt.eclipse.org", 1883,60)  
        
        jsonData = self.getSensorData()
        logging.info("SensorData befor publishing: " + jsonData)
        self.client.loop_start()
        
        self.client.publish("kai_test", jsonData, 2, True)
        self.client.loop_stop()
        self.client.disconnect()
        
        
        self.client.subscribe("kai_test", 2)



