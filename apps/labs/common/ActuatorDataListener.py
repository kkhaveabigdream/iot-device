'''
Created on Feb 19, 2020

@author: sk199
'''
#from labs.common.PersistenceUtil import PersistenceUtil
import redis
from labs.module05.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.DataUtil import DataUtil
import logging

class ActuatorDataListener(object):
    '''
    classdocs
    '''
    #persistenceUtil = PersistenceUtil()
    dataUtil = DataUtil()
    multiActuatorAdaptor = MultiActuatorAdaptor()
    actuatorData = None

    def __init__(self):
        '''
        Constructor
        '''
        self.r = redis.Redis(host='localhost', port=6379)
        
    def listener(self):
        pubsub = self.r.pubsub()
        pubsub.subscribe('ActuatorData')
        
        #print("Starting message loop")
        while (True):
            message = pubsub.get_message()
            if message:
                #sensorDataJson = self.persistenceUtil.getSensorData()
                #print(message)
                
                #print(message['data'])
                
                if(type(message['data'])!=int):
                    logging.info("Listening on Redis, jsonActuatorData retrieved from Redis...")
                    logging.info("ActuatorData: " + str(message['data']))
                    print("---------------------------")
                    self.actuatorData = self.dataUtil.toActuatorDataFromJson(message['data'])
                    #print(self.actuatorData.Command)
                    self.multiActuatorAdaptor.updateActuator(self.actuatorData)