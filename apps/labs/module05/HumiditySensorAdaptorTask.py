'''
Created on Feb 13, 2020

@author: sk199
'''


from sense_hat import SenseHat



class HumiditySensorAdaptorTask():
    rateInSec = 10
    curHumid = 0
    
    sense = SenseHat()


    
    '''
    Read the Humidity data from the SenseHAT
    '''

    def __init__(self):
        self.time      = self.sensorData.timeStamp 
        
    def getHumidity(self):
        self.curHumid = self.sense.get_humidity()
        return self.curHumid
    

            
        