'''
Created on Feb 5, 2020

@author: sk199
'''

from labs.common.ActuatorData import ActuatorData
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst
import logging
from project.SmtpClientConnector import SmtpClientConnector
from labs.module06.MultiActuatorAdaptor import MultiActuatorAdaptor


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
        self.config.loadConfig()
#         self.nominalTemp = float(self.config.getValue(ConfigConst.DEVICE, ConfigConst.NOMINAL_TEMP))
#         self.nominalHumid= float(self.config.getValue(ConfigConst.DEVICE, ConfigConst.NOMINAL_HUMID))
        self.time       = sensorData.timeStamp                                     
        self.average    = sensorData.avgValue
        self.samples    = sensorData.getCount()
        self.min        = sensorData.minValue
        self.max        = sensorData.maxValue        
        self.name       = sensorData.getName()
        
        if (self.name == 'Temp'):
            self.message    = 'Temperature\n' + '\tTime: ' +str(self.time) + '\n\tCurrent: ' + str(sensorData.curValue) + '\n\tAverage: ' +str(self.average) + '\n\tSamples: ' + str(self.samples) + '\n\tMin: ' + str(self.min) + '\n\tMax: ' + str(self.max)
            if(sensorData.curValue>20):
            
                logging.info('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')
                #print('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')      
                
                self.connector.publishMessage('Excessive Temperature', self.message)
                self.actuatorData.setCommand('Increasing')
                self.actuatorData.getValue(sensorData.curValue)
                self.multiActuator.updateActuator(self.actuatorData)
                print(self.message)
                return(self.actuatorData)
            
            
            elif(sensorData.curValue<20):
                
                logging.info('\nCurrent temperature lower than nonminalTemp by < ' +str(self.nominalTemp) + '. Triggering alert...')                                     
                 
                self.connector.publishMessage('Decreasing Temperature', self.message)
                self.actuatorData.setCommand('Decreasing')
                self.actuatorData.getValue(sensorData.curValue)
                self.multiActuator.updateActuator(self.actuatorData)
                print(self.message)
                return(self.actuatorData)
            
            else:
                return(None)
        
        if (self.name == 'SoilMoisture'):
            self.message    = 'SoilMoisture\n' + '\tTime: ' +str(self.time) + '\n\tCurrent: ' + str(sensorData.curValue) + '\n\tAverage: ' +str(self.average) + '\n\tSamples: ' + str(self.samples) + '\n\tMin: ' + str(self.min) + '\n\tMax: ' + str(self.max)
            if(sensorData.curValue>20):
            
                logging.info('\nCurrent humidity exceeds nonminalHumid by > ' +str(20) + '. Triggering alert...')
                #print('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')      
                
                self.connector.publishMessage('Moist Humidity', self.message)
#                 self.actuatorData.setCommand('sensehatMoist')
#                 self.actuatorData.getValue(sensorData.curValue)
#                 self.multiActuator.updateActuator(self.actuatorData)
#                 print(self.message)
#                 return(self.actuatorData)
            
            
            elif(sensorData.curValue<20):
                
                logging.info('\nCurrent Humidity lower than nonminalHumid by < ' +str(20) + '. Triggering alert...')                                     
                 
                self.connector.publishMessage('Dry Humidity', self.message)
#                 self.actuatorData.setCommand('sensehatDry')
#                 self.actuatorData.getValue(sensorData.curValue)
#                 self.multiActuator.updateActuator(self.actuatorData)
#                 print(self.message)
#                 return(self.actuatorData)
#             
#             else:
#                 return(None)    
#             
        if (self.name == 'I2C_Humid'):
            self.message    = 'I2C Direct Humidity\n' + '\tTime: ' +str(self.time) + '\n\tCurrent: ' + str(sensorData.curValue) + '\n\tAverage: ' +str(self.average) + '\n\tSamples: ' + str(self.samples) + '\n\tMin: ' + str(self.min) + '\n\tMax: ' + str(self.max)
            if(sensorData.curValue>20):
            
                logging.info('\nCurrent humidity exceeds nonminalHumid by > ' +str(self.nominalHumid) + '. Triggering alert...')
                #print('\nCurrent temperature exceeds nonminalTemp by > ' +str(self.nominalTemp) + '. Triggering alert...')      
                
                self.connector.publishMessage('Moist Humidity', self.message)
                self.actuatorData.setCommand('i2cMoist')
                self.actuatorData.getValue(sensorData.curValue)
                self.multiActuator.updateActuator(self.actuatorData)
                print(self.message)
                return(self.actuatorData)
            
            
            elif(sensorData.curValue<20):
                
                logging.info('\nCurrent Humidity lower than nonminalHumid by < ' +str(self.nominalTemp) + '. Triggering alert...')                                     
                 
                self.connector.publishMessage('Dry Humidity', self.message)
                self.actuatorData.setCommand('i2cDry')
                self.actuatorData.getValue(sensorData.curValue)
                self.multiActuator.updateActuator(self.actuatorData)
                print(self.message)
                return(self.actuatorData)
            
            else:
                return(None)        
            