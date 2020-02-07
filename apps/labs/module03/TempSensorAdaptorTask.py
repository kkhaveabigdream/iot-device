'''
Created on Feb 5, 2020

@author: sk199
'''
import threading
from labs.common.SensorData import SensorData
from sense_hat import SenseHat
from time import sleep


class TempSensorAdaptorTask(threading.Thread):
    rateInSec = 10
    curTemp = 0
    sensorData = SensorData()
    sense = SenseHat()


    def __init__(self, rateInSec=10):
        threading.Thread.__init__(self)
        self.rateInSec = rateInSec
        
    def getTemperature(self):
        self.curTemp = self.sense.get_temperature()
        return self.curTemp
    
    def run(self):
        while True:
            self.sensorData.addValue(self.getTemperature())
            sleep(self.rateInSec)
    