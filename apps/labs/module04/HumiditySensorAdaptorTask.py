'''
Created on Feb 13, 2020

@author: sk199
'''

import threading
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
from time import sleep
from labs.module04.SensorDataManager import SensorDataManager


class HumiditySensorAdaptorTask(threading.Thread):
    rateInSec = 10
    curHumid = 0
    sensorData = SensorData()
    sense = SenseHat()
    manager = SensorDataManager()
    
    '''
    Read the Temperature from the SenseHAT
    '''

    def __init__(self, rateInSec=10):
        threading.Thread.__init__(self)
        self.rateInSec = rateInSec
        self.time      = self.sensorData.timeStamp 
        
    def getHumidity(self):
        self.curHumid = self.sense.get_Humidity()
        return self.curHumid
    
    def run(self):
        while True:
            print("SenseHat API Humidity " + str(self.curHumid))
            self.sensorData.addValue(self.getHumidity())
            #print(self.sensorData.curValue)
            self.manager.handleSensorData(self.sensorData)
            
            sleep(self.rateInSec)
        