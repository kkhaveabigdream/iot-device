'''
Created on Jan 28, 2020

@author: sk199
'''
import configparser
from os.path import os


class ConfigUtil(object):
    '''
    classdocs
    '''
    configData = configparser.ConfigParser()
    configFile = '../../../config/ConnectedDevicesConfig.props'

    def __init__(self):
        
        '''
        Constructor
        '''
    
    def loadConfig(self,configFile= configFile):
       
        self.configFile = configFile
        self.configData.read(self.configFile)
        secs = self.configData.sections()       
       #print(secs)
        for i in secs:   
            kvs = self.configData.items(i)
            print(kvs)
        
        if(kvs):
            self.isLoaded = True
        else:
            self.isLoaded = False
        
        '''
        if(os.path.exists(self.configFile)):
            return True
        else:
            return False
        '''
    def hasConfigData(self):
        if(self.isLoaded):
            print("Config is Loaded")
        else:
            print("Config failed")
        return self.isLoaded
            
   
        
   
    
test=ConfigUtil()
test.loadConfig()
test.hasConfigData()