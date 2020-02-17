'''
Created on Feb 13, 2020

@author: sk199
'''

import threading
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
from time import sleep
from labs.module04.SensorDataManager import SensorDataManager
from labs.module04.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask


class HumiditySensorAdaptorTask(threading.Thread):
    rateInSec = 10
    curHumid = 0
    sensorData = SensorData()
    sense = SenseHat()
    manager = SensorDataManager() 
    i2cHumid = HI2CSensorAdaptorTask()
    enableHumidSensor = False
    
    '''
    Read the Humidity data from the SenseHAT
    '''

    def __init__(self, rateInSec=10):
        threading.Thread.__init__(self)
        self.rateInSec = rateInSec
        self.time      = self.sensorData.timeStamp 
        
    def getHumidity(self):
        self.curHumid = self.sense.get_humidity()
        return self.curHumid
    
    def run(self):
        while True:
            if self.enableHumidSensor:
                self.sensorData.setName("Humid")                
                self.sensorData.addValue(self.getHumidity())
                #print(str(datetime.now()) + "SenseHat API Humidity   " + str(self.curHumid))
                #print(str(datetime.now()) + "I2C Direct Humidity:    " + str(self.i2cHumid.getHumidityData()))
                ##print(self.sensorData.curValue)
                self.manager.handleSensorData(self.sensorData)
                
                sleep(self.rateInSec)
        