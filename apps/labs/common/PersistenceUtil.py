'''
Created on Feb 19, 2020

@author: sk199
'''
import redis
from labs.common.DataUtil import DataUtil

class PersistenceUtil(object):
    '''
    classdocs
    '''
    datautil = DataUtil()


    def __init__(self):
        '''
        Constructor
        '''
        self.r = redis.Redis(host='localhost', port=6379)
        
    def writeSensorDataToRedis(self,SensorData):
        jsondata = self.datautil.toJsonFromSensorData(SensorData)
        #self.r.lpush("SensorData", jsondata)
        self.r.publish("SensorData", jsondata)
        
    def writeActuatorDataToRedis(self,ActuatorData):
        jsondata = self.datautil.toJsonFromActuatorData(ActuatorData)
        #self.r.lpush("ActuatorData", jsondata)
        self.r.publish("ActuatorData", jsondata)
    
    def getSensorData(self):
        sensorData = self.r.get("SensorData")
        return sensorData