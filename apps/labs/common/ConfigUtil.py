'''
Created on Jan 28, 2020

@author: sk199
'''
import configparser



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
            print("has configData")
        else:
            print("configData is NULL")
        return self.isLoaded
    
    def getValue(self,section,part):
        self.section = section
        self.part = part
        self.configValue = self.configData.get(self.section, self.part)
        print(self.configValue)
        return self.configValue
            
   
        
   
    
test=ConfigUtil()
test.loadConfig()
test.hasConfigData()
test.getValue("smtp.cloud","port")