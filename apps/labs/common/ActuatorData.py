'''
Created on Feb 5, 2020

@author: sk199
'''
from _datetime import datetime
from labs.common.SensorData import SensorData


class ActuatorData(object):
    '''
    classdocs
    '''
    timeStamp = None
    Command = ''
    Value = 0.0
    Name = ''
    sensordata = SensorData()
    


    def __init__(self):
        self.timeStamp = str(datetime.now())
    
    def setCommand(self,command):
        self.Command = command
    
    def getCommand(self):
        return self.Command
    
    def setName(self,sensorName):
        self.Name = sensorName
        
    def getName(self):
        return self.Name
    
    def getValue(self):
        self.value = self.sensordata.getCurrentValue()
        return self.value