'''
Created on Feb 5, 2020

@author: sk199
'''

from labs.common.ActuatorData import ActuatorData
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst
import logging
from labs.module02.SmtpClientConnector import SmtpClientConnector
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor

class SensorDataManager(object):
    '''
    classdocs
    '''
    alertDiff = 0
    actuatorData = ActuatorData()
    

    def __init__(self, altertDiff = 5):
        '''
        Constructor
        '''
        self.config = ConfigUtil()
        self.connector = SmtpClientConnector()
        self.tempActuator = TempActuatorAdaptor()
        
    
    def handleSensorData(self,sensorData):
        self.nominalTemp = float(self.config.getValue(ConfigConst.DEVICE, ConfigConst.NOMINAL_TEMP))
        self.time       = sensorData.timeStamp                                     
        self.average    = sensorData.avgValue
        self.samples    = sensorData.getCount()
        self.min        = sensorData.minValue
        self.max        = sensorData.maxValue 
        self.message    = 'Temperature\n' + '\tTime: ' +str(self.time) + '\n\tCurrent: ' + str(sensorData.curValue) + '\n\tAverage: ' +str(self.average) + '\n\tSamples: ' + str(self.samples) + '\n\tMin: ' + str(self.min) + '\n\tMax: ' + str(self.max)
        
        if(sensorData.curValue>self.nominalTemp):
            
            logging.info('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')
            #print('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')      
            
            self.connector.publishMessage('Excessive Temperature', self.message)
            self.actuatorData.setCommand('Increasing')
            self.actuatorData.getValue(sensorData.curValue)
            self.tempActuator.updateActuator(self.actuatorData)
            print(self.message)
            
            
        elif(sensorData.curValue<self.nominalTemp):
            
            logging.info('\nCurrent temperature falls below nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')                                     
             
            self.connector.publishMessage('Decreasing Temperature', self.message)
            self.actuatorData.setCommand('Decreasing')
            self.actuatorData.getValue(sensorData.curValue)
            self.tempActuator.updateActuator(self.actuatorData)
            print(self.message)
            