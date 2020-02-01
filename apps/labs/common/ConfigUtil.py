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
    

    # configFile represents the relative file name to load. If null or empty,default will be used. 
    def loadConfig(self,configFile= configFile):
       
        self.configFile = configFile
        self.configData.read(self.configFile)
        secs = self.configData.sections()       
        #print(secs)
        for i in secs:   
            kvs = self.configData.items(i)
            #print(kvs)
        
        if(kvs):
            self.isLoaded = True
            return True
        else:
            self.isLoaded = False
            return False
                
    
    #Returns true if, after loadConfig() is called, there is any valid key / value configuration data pair within any section .
    def hasConfigData(self):
        if(self.isLoaded):
            print("has configData")
        else:
            print("configData is NULL")
        return self.isLoaded
    

    #The first parameter is 'section', which represents the config file section to parse. The second parameter is 'key',
    #which represents the key of the value within the given section to return
    def getValue(self,section,part):
        self.section = section
        self.part = part
        self.configValue = self.configData.get(self.section, self.part)
        #print(self.configValue)
        return self.configValue
            
   
        
   
    
# test=ConfigUtil()
# test.loadConfig()
# test.hasConfigData()
# test.getValue("smtp.cloud","port")