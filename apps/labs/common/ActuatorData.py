'''
Created on Feb 5, 2020

@author: sk199
'''
from _datetime import datetime


class ActuatorData(object):
    '''
    classdocs
    '''
    timeStamp = None
    Command = ''
    Value = 0.0
    Name = ''
    
    '''
    Capture the new state for the actuator
    '''

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
    
    def getValue(self,curValue):
        self.Value = curValue