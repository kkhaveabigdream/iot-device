'''
Created on Jan 28, 2020

@author: sk199
'''
import random
import threading
from time import sleep
from labs.common.SensorData import SensorData
import logging
from labs.module02.SmtpClientConnector import SmtpClientConnector

class TempSensorEmulatorTask(threading.Thread):
    '''
    classdocs
    '''
    rateInSec = 10
    alertDiff = 0
    sensorData = SensorData()
    enableEmulator = False
    message = ''


    def __init__(self,rateInSec=5,alertDiff = 5):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.connector  = SmtpClientConnector()
        self.rateInSec  = rateInSec
        self.alertDiff  = alertDiff
        self.time       = self.sensorData.timeStamp        
#         self.average    = self.sensorData.avgValue
#         self.samples    = self.sensorData.getCount()
#         self.min        = self.sensorData.minValue
#         self.max        = self.sensorData.maxValue
#         
    '''
    randomly generating a temperature value between 0 C and 30 C, return a reference to SensorData. 
    '''  
    def getSensorData(self):
        self.curValue = round(random.uniform(0.0,30.0),2)
        #print(self.curValue)
        return self.curValue
    '''
    Check if the randomly generated value is different from the average stored measurement by a configurable threshold(5)
    If the threshold is reached or surpassed, the most recent SensorData (and any other information) 
    will be emailed to a remote service using the SmtpClientConnector module
    '''
    def sendNotification(self):
        if (abs(self.sensorData.curValue-self.sensorData.getAverageValue()) >=self.alertDiff):            
            logging.info('\nCurrent temperature exceeds average by > ' +str(self.alertDiff) + '. Triggering alert...')                                     
            self.average    = self.sensorData.avgValue
            self.samples    = self.sensorData.getCount()
            self.min        = self.sensorData.minValue
            self.max        = self.sensorData.maxValue       
            self.message    = 'Temperature\n' + '\tTime: ' +str(self.time) + '\n\tCurrent: ' + str(self.curValue) + '\n\tAverage: ' +str(self.average) + '\n\tSamples: ' + str(self.samples) + '\n\tMin: ' + str(self.min) + '\n\tMax: ' + str(self.max)
            self.connector.publishMessage('Excessive Temperature', self.message)
            print(self.message)  
            #self.connector.publishMessage('Excessive Temperature', self.curValue)
    
    def run(self):
        while True:                      
            self.sensorData.addValue(self.getSensorData())
            #print(self.sensorData.curValue)
            #print(self.sensorData.getCurrentValue())
            #print(self.sensorData.getCount())
            #print(self.sensorData.getAverageValue())
            self.sendNotification()  
            #print(self.message)                     
            sleep(self.rateInSec)

           

# t=TempSensorEmulatorTask()
# t.start()

