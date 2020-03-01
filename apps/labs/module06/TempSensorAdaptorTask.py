'''
Created on Feb 5, 2020

@author: sk199
'''


from sense_hat import SenseHat




class TempSensorAdaptorTask():
    
    curTemp = 0
    
    sense = SenseHat()
    
    
    
    '''
    Read the Temperature from the SenseHAT
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        
    def getTemperature(self):
        self.curTemp = self.sense.get_temperature()
        return self.curTemp
    
    
        