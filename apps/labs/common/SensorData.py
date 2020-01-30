'''
Created on Jan 28, 2020

@author: sk199
'''
from _datetime import datetime



class SensorData():
    '''
    classdocs
    '''
    timeStamp   = None
    name        = 'Not set'
    curValue    = 0   
    avgValue    = 0
    minValue    = 0
    maxValue    = 0
    totValue    = 0
    sampleCount = 0 
    
    

    def __init__(self):
        self.timeStamp = str(datetime.now())
        
        
    def addValue(self,newVal):
        self.sampleCount += 1
        self.curValue = newVal
        self.totValue += newVal
        
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
            
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
        
        if (self.totValue !=0 and self.sampleCount >0):
            self.avgValue = self.totValue/self.sampleCount
            
    def getAverageValue(self):
        return self.avgValue
    
    def getCount(self):
        return self.sampleCount
    
    def getCurrentValue(self):
        return self.curValue
    
    def getMinValue(self):
        return self.minValue
    
    def getMaxValue(self):
        return self.maxValue
    
    def getName(self):
        return self.name
    
    def setName(self,sensorName):
        self.name = sensorName
        





    
    
    
    


        