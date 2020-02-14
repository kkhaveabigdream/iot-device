'''
Created on Feb 13, 2020

@author: sk199
'''

import threading


#import smbus2
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst

#i2cBus          = smbus2.SMBus(1)

enableControl   = 0x2D
enableMeasure   = 0x08

accelAddr       = 0x1C
magAddr         = 0x6A
pressAddr       = 0x5C
humidAddr       = 0x5F

begAddr         = 0x28
totBytes        = 6

DEFAULT_RATE_IN_SEC = 5

class HI2CSensorAdaptorTask(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self):
        super(HI2CSensorAdaptorTask,self).__init__()
        
        self.config = ConfigUtil()
        self.config.loadConfig(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        
        print('Configuration data...\n' + str(ConfigConst.DEFAULT_CONFIG_FILE_NAME))
        
test = HI2CSensorAdaptorTask()
