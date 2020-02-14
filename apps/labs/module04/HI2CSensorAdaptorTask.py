'''
Created on Feb 13, 2020

@author: sk199
'''

import threading


import smbus2
from labs.common.ConfigUtil import ConfigUtil
from labs.common import ConfigConst
import logging
from time import sleep


i2cBus          = smbus2.SMBus(1)

enableControl   = 0x2D
enableMeasure   = 0x08

accelAddr       = 0x1C
magAddr         = 0x6A
pressAddr       = 0x5C
humidAddr       = 0x5F

begAddr         = 0x28
totBytes        = 6

DEFAULT_RATE_IN_SEC = 5
rateInSec           = 5

class HI2CSensorAdaptorTask(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self,rateInSec = 5):
        super(HI2CSensorAdaptorTask,self).__init__()
        
        self.rateInSec = rateInSec
        self.config = ConfigUtil()
        self.config.loadConfig(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        
        print('Configuration data...\n' + str(ConfigConst.DEFAULT_CONFIG_FILE_NAME))
        
    def initI2CBus(self):
        logging.info("Initializing I2C bus and enabling I2C addresses...")
        
        i2cBus.write_byte_data(accelAddr, 0, 0)
        i2cBus.write_byte_data(magAddr,0,0)
        i2cBus.write_byte_data(pressAddr,0,0)
        i2cBus.write_byte_data(humidAddr,0,0)
        
    def displayAccelerometerData(self):
        acceleData = i2cBus.read_byte_data(accelAddr, begAddr, totBytes)
        print(acceleData)
        
    def displayMagnetometerData(self):
        magData = i2cBus.read_byte_data(magAddr, begAddr, totBytes)
        print(magData)
    
    def displayPressureData(self):
        pressureData = i2cBus.read_byte_data(pressAddr, begAddr, totBytes)
        print(pressureData)
        
    def displayHumidityData(self):
        humidityData = i2cBus.read_byte_data(humidAddr, begAddr, totBytes)
        print(humidityData)
        
    def run(self):
        while True:
            self.displayAccelerometerData()
            self.displayMagnetometerData()
            self.displayPressureData()
            self.displayHumidityData()
            
            sleep(self.rateInSec)
        
        
test = HI2CSensorAdaptorTask()
