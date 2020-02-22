'''
Created on Feb 5, 2020

@author: sk199
'''
from labs.module05.SenseHatLedActivator import SenseHatLedActivator

class MultiActuatorAdaptor(object):
    '''
    classdocs
    '''
    curTemp     = 0
    curHumid    = 0


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
        
        elif(actuatorData.getCommand()=='sensehatMoist'):
            self.curHumid = round(actuatorData.Value, 2)
            self.shLed.run3(self.curHumid)
            
        elif(actuatorData.getCommand()=='sensehatDry'):
            self.curHumid = round(actuatorData.Value, 2)
            self.shLed.run4(self.curHumid)
            
        elif(actuatorData.getCommand()=='i2cMoist'):
            self.curHumid = round(actuatorData.Value, 2)
            self.shLed.run5(self.curHumid)
                                
        elif(actuatorData.getCommand()=='i2cDry'):
            self.curHumid = round(actuatorData.Value, 2)    
            self.shLed.run6v (self.curHumid)            
            
            
            