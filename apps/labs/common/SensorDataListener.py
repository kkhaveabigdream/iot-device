'''
Created on Feb 19, 2020

@author: sk199
'''
import redis
import time
from labs.common.PersistenceUtil import PersistenceUtil


class SensorDataListener(object):
    '''
    classdocs
    '''
    persistenceUtil = PersistenceUtil()
   

    def __init__(self):
        '''
        Constructor
        '''
        self.r = redis.Redis(host='localhost', port=6379)
        
        
    def listener(self):
        pubsub = self.r.pubsub()
        pubsub.subscribe('SensorData')
        
        print("Starting message loop")
        while (True):
            message = pubsub.get_message()
            if message:
                #sensorDataJson = self.persistenceUtil.getSensorData()
                print(message['data'])
            
    
        