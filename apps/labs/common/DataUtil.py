'''
Created on Feb 19, 2020

@author: sk199
'''
import json
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData



class DataUtil(object):
    '''
    classdocs
    '''
    jsonData = None


    def __init__(self):
        '''
        Constructor
        '''
        
    def toJsonFromSensorData(self,SensorData):
        jsonData = json.dumps(SensorData.__dict__)
        #print('-->')
        #print(jsonData)
        return jsonData
        
        
        
    def toSensorDataFromJson(self,jsonData):
        sdDict = json.loads(jsonData)
        print(" decode [pre] --> " + str(sdDict))
        
        sd              = SensorData()
        sd.name         = sdDict['name']
        sd.timeStamp    = sdDict['timeStamp']
        sd.avgValue     = sdDict['avgValue']
        sd.minValue     = sdDict['minValue']
        sd.maxValue     = sdDict['maxValue']
        sd.curValue     = sdDict['curValue']
        sd.totValue     = sdDict['totValue']
        sd.sampleCount  = sdDict['sampleCount']
        
        print(" decode [post] --> " + str(sd))
        
        return sd
                                      
      
    def writeSensorDataToFile(self,SensorData): 
        with open('sensorData.json','w') as file:
            json.dump(SensorData.__dict__, file)
            
               
      
    def toJsonFromActuatorData(self,ActuatorData):
        jsonData = json.dumps(ActuatorData.__dict__)
        #print('-->')
        #print(jsonData)
        return jsonData
        
          
    def toActuatorDataFromJson(self,jsonData):
        adDict = json.loads(jsonData)
        
        #print(" decode [pre] --> " + str(adDict))
        
        ad              = ActuatorData()
        ad.Name         = adDict['name']
        ad.timeStamp    = adDict['timeStamp']
        ad.Command      = adDict['command']
        ad.Value        = adDict['curValue']
        ad.Value        = adDict['value']
        ad.timeStamp    = adDict['timestamp']
        
        #print(" decode [post] --> " + str(ad))
        
        return ad
    
    def toActuatorDataFromJson2(self,jsonData):
        adDict = json.loads(jsonData)
        
        ad              = ActuatorData()
        ad.Value        = adDict['value']
        ad.timeStamp    = adDict['timestamp']
        
        #print(" decode [post] --> " + str(ad))
        
        return ad
         
           
    def writeActuatorDataToFile(self,ActuatorData):
        with open('actuatorData.json','w') as file:
            json.dump(ActuatorData.__dict__, file)
         
    
