'''
Created on Feb 5, 2020

@author: sk199
'''
from labs.module03.SenseHatLedActivator import SenseHatLedActivator

class TempActuatorAdaptor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.shLed = SenseHatLedActivator()
    
    def updateActuator(self,actuatorData):
        if(actuatorData.getCommand()=='Increasing'):
            self.shLed.run()
            
        elif(actuatorData.getCommand()=='Decreasing'):
            self.shLed.run2()
            