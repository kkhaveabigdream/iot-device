'''
Created on Feb 5, 2020

@author: sk199
'''
from labs.module04.SenseHatLedActivator import SenseHatLedActivator

class MultiActuatorAdaptor(object):
    '''
    classdocs
    '''
    curTemp = 0


    def __init__(self):
        '''
        Constructor
        '''
        self.shLed = SenseHatLedActivator()
    '''
    Access the SenseHAT'S LED matrix
    Trigger LED model 1 if get Temperature Increasing command
    Trigger LED model 2 if get Temperature Decreasing command
    '''
    
    def updateActuator(self,actuatorData):
        if(actuatorData.getCommand()=='Increasing'):
            self.curTemp = round(actuatorData.Value,2)
            self.shLed.run(self.curTemp)
            
        elif(actuatorData.getCommand()=='Decreasing'):
            self.curTemp = round(actuatorData.Value,2)
            self.shLed.run2(self.curTemp)
            