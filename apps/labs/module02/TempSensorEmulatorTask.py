'''
Created on Jan 28, 2020

@author: sk199
'''
import random
import threading
from time import sleep
from labs.common.SensorData import SensorData
import logging

class TempSensorEmulatorTask(threading.Thread):
    '''
    classdocs
    '''
    rateInSec = 10
    alertDiff = 0
    sensorData = SensorData()


    def __init__(self,rateInSec=3,alertDiff = 5):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        #super(TempSensorEmulatorTask,self).__init__()
        self.rateInSec = rateInSec
        self.alertDiff = alertDiff
    
    def getSensorData(self):
        self.curValue = round(random.uniform(0.0,30.0),2)
        #print(self.curValue)
        return self.curValue
    
    def sendNotification(self):
        if (abs(self.sensorData.curValue-self.sensorData.getAverageValue()) >=self.alertDiff):
            logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
            logging.info('\n Current temp exceeds average by >' +str(self.alertDiff) + '. Triggering alert...')
            #print('\n Current temp exceeds average by >' +str(self.alertDiff) + '. Triggering alert...')
    
    def run(self):
        while True:                      
            self.sensorData.addValue(self.getSensorData())
            print(self.sensorData.curValue)
            #print(self.sensorData.getCurrentValue())
            print(self.sensorData.getCount())
            print(self.sensorData.getAverageValue())
            self.sendNotification()
                       
            sleep(self.rateInSec)

           

t=TempSensorEmulatorTask()
t.start()

