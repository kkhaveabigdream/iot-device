'''
Created on Feb 5, 2020

@author: sk199
'''


from project.mcp3008 import mcp3008




class SoilMoistureSensorAdaptorTask():
    
    curMoisture = 0
    
    sense = mcp3008()
    
    
    
    '''
    Read the Temperature from the SenseHAT
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        
    def getSoilMoisture(self):
        self.curMoisture = self.sense.getAdc(0)
        return self.curMoisture
    
    
        