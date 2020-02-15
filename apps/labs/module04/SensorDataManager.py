'''
Created on Feb 5, 2020

@author: sk199
'''

from labs.common.ActuatorData import ActuatorData
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst
import logging
from labs.module02.SmtpClientConnector import SmtpClientConnector
from labs.module04.MultiActuatorAdaptor import MultiActuatorAdaptor


class SensorDataManager(object):
    '''
    classdocs
    '''   
    actuatorData = ActuatorData()
    
    

    def __init__(self):
        '''
        Constructor
        '''
        self.config = ConfigUtil()
        self.connector = SmtpClientConnector()
        self.multiActuator = MultiActuatorAdaptor()
        
    '''
    If current temperature exceeds or falls below the 'nominalTemp', the new SensorData instance will trigger an actuation
    It will return the new ActualatorData instance with the appropriate data value and command embedded;
    Otherwise, it returns None
    Also,if an actuation is triggered, the SmtpClientConnector instance will be created to send the e-mail 
    message to the appropriate destination    
    '''
        
    def handleSensorData(self,sensorData):
        self.nominalTemp = float(self.config.getValue(ConfigConst.DEVICE, ConfigConst.NOMINAL_TEMP))
        self.time       = sensorData.timeStamp                                     
        self.average    = sensorData.avgValue
        self.samples    = sensorData.getCount()
        self.min        = sensorData.minValue
        self.max        = sensorData.maxValue 
        self.message    = 'Temperature\n' + '\tTime: ' +str(self.time) + '\n\tCurrent: ' + str(sensorData.curValue) + '\n\tAverage: ' +str(self.average) + '\n\tSamples: ' + str(self.samples) + '\n\tMin: ' + str(self.min) + '\n\tMax: ' + str(self.max)
        self.name       = sensorData.getName()
        
        if (self.name == 'Temp'):
            if(sensorData.curValue>self.nominalTemp):
            
                logging.info('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')
                #print('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')      
                
                self.connector.publishMessage('Excessive Temperature', self.message)
                self.actuatorData.setCommand('Increasing')
                self.actuatorData.getValue(sensorData.curValue)
                self.multiActuator.updateActuator(self.actuatorData)
                print(self.message)
                return(self.actuatorData)
            
            
            elif(sensorData.curValue<self.nominalTemp):
                
                logging.info('\nCurrent temperature falls below nonminalTemp by < ' +str(self.nominalTemp) + '. Triggering alert...')                                     
                 
                self.connector.publishMessage('Decreasing Temperature', self.message)
                self.actuatorData.setCommand('Decreasing')
                self.actuatorData.getValue(sensorData.curValue)
                self.multiActuator.updateActuator(self.actuatorData)
                print(self.message)
                return(self.actuatorData)
            
            else:
                return(None)
            