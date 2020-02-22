'''
Created on Feb 5, 2020

@author: sk199
'''
import threading
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
from time import sleep
from labs.module03.SensorDataManager import SensorDataManager
from labs.common.DataUtil import DataUtil


class TempSensorAdaptorTask(threading.Thread):
    rateInSec = 10
    curTemp = 0
    sensorData = SensorData()
    sense = SenseHat()
    manager = SensorDataManager()
    dataUtil = DataUtil()
    
    '''
    Read the Temperature from the SenseHAT
    '''

    def __init__(self, rateInSec=10):
        threading.Thread.__init__(self)
        self.rateInSec = rateInSec
        self.time      = self.sensorData.timeStamp 
        
    def getTemperature(self):
        self.curTemp = self.sense.get_temperature()
        return self.curTemp
    
    def run(self):
        while True:
            self.sensorData.setName('Temp')
            self.sensorData.addValue(self.getTemperature())
            #print(self.sensorData.curValue)
            self.manager.handleSensorData(self.sensorData)
            
            self.dataUtil.toJsonFromSensorData(self.sensorData)
            
            sleep(self.rateInSec)
    