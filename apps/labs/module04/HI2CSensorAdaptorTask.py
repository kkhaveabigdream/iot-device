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
from labs.common.SensorData import SensorData
from labs.module04.SensorDataManager import SensorDataManager
from _datetime import datetime


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
    RH = 0 
    sensorData = SensorData()
    manager = SensorDataManager()
    enableHI2CSensor = False

    def __init__(self,rateInSec = 10):
        super(HI2CSensorAdaptorTask,self).__init__()
        
        self.rateInSec = rateInSec
        self.config = ConfigUtil()
        self.config.loadConfig(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        
        print('Configuration data...\n' + str(ConfigConst.DEFAULT_CONFIG_FILE_NAME))
        
    def initI2CBus(self):
        logging.info("Initializing I2C bus and enabling I2C addresses...")
        
        i2cBus.write_byte_data(accelAddr, enableControl, enableMeasure)
        i2cBus.write_byte_data(magAddr,enableControl, enableMeasure)
        i2cBus.write_byte_data(pressAddr,enableControl, enableMeasure)
        i2cBus.write_byte_data(humidAddr,enableControl, enableMeasure)
        
    def displayAccelerometerData(self):
        acceleData = i2cBus.read_i2c_block_data(accelAddr, begAddr, totBytes)
        print("Accelerometer block data:    " + str(acceleData))
        
    def displayMagnetometerData(self):
        magData = i2cBus.read_i2c_block_data(magAddr, begAddr, totBytes)
        print("Magnetometer block data:     " + str(magData))
        
    
    def displayPressureData(self):
        pressureData = i2cBus.read_i2c_block_data(pressAddr, begAddr, totBytes)
        print("Pressure block data:         " + str(pressureData))
        
        
    def displayHumidityData(self):
        humidityData = i2cBus.read_i2c_block_data(humidAddr, begAddr, totBytes)
        print("Humidity block data:         " + str(humidityData))
    
    ''' 
    Read the data from I2C bus. 
    Combine the LSB and MSB data into a human readable float representing humidity from the sensor   
    ''' 
    def getHumidityData(self):
        bits = 8
        
        coeffH0 = i2cBus.read_byte_data(humidAddr, 0x30)  >> 1
        coeffH1 = i2cBus.read_byte_data(humidAddr, 0x31)  >> 1
        h0_rh   = coeffH0
        h1_rh   = coeffH1
        
        valH0T0a = i2cBus.read_byte_data(humidAddr, 0x36)
        valH0T0b = i2cBus.read_byte_data(humidAddr, 0x37)
        valH0T0  = (valH0T0b<<bits) | valH0T0a
        if valH0T0 & (1 << 16 - 1):
            valH0T0 -=(1 << 16)
        
        valH1T0a = i2cBus.read_byte_data(humidAddr, 0x3A)
        valH1T0b = i2cBus.read_byte_data(humidAddr, 0x3B)
        valH1T0  = (valH1T0b<<bits) | valH1T0a
        if valH1T0 & (1 << 16 - 1):
            valH1T0 -=(1 << 16)
        
        valHTa    = i2cBus.read_byte_data(humidAddr, 0x28)
        valHTb    = i2cBus.read_byte_data(humidAddr, 0x29)
        valHT     = (valHTb<<bits) | valHTa
        if valHT & (1 << 16 - 1):
            valHT -=(1 << 16)
        
        self.RH = (((h1_rh-h0_rh)*(valHT-valH0T0))/(valH1T0-valH0T0)) + h0_rh
        
        return(self.RH)
        
        
        
    def run(self):
        while True:
            if self.enableHI2CSensor:
                self.displayAccelerometerData()
                self.displayMagnetometerData()
                self.displayPressureData()
                self.displayHumidityData()
                self.getHumidityData()
                #print(str(datetime.now()) + "I2C Direct Humidity:    " + str(self.RH))
                self.sensorData.setName("I2C_Humid")
                self.sensorData.addValue(self.RH)
                self.manager.handleSensorData(self.sensorData)
                
                sleep(self.rateInSec)
        
    
        
        
        
        
        
        
        
        
#test = HI2CSensorAdaptorTask()
