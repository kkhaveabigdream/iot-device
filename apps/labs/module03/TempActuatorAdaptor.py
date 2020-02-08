'''
Created on Feb 5, 2020

@author: sk199
'''
from labs.module03.SenseHatLedActivator import SenseHatLedActivator

class TempActuatorAdaptor(object):
    '''
    classdocs
    '''
    curTemp = 0


    def __init__(self):
        '''
        Constructor
        '''
        self.shLed = SenseHatLedActivator()
    
    def updateActuator(self,actuatorData):
        if(actuatorData.getCommand()=='Increasing'):
            self.curTemp = actuatorData.Value
            self.shLed.run(self.curTemp)
            
        elif(actuatorData.getCommand()=='Decreasing'):
            self.curTemp = actuatorData.Value
            self.shLed.run2(self.curTemp)
            