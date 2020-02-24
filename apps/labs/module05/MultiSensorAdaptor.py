'''
Created on Feb 5, 2020

@author: sk199
'''
from time import sleep
import threading
from labs.common.SensorData import SensorData
from labs.module05.SensorDataManager import SensorDataManager
from labs.module05.TempSensorAdaptorTask import TempSensorAdaptorTask
# from labs.module05.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
# from labs.module05.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask
from labs.common.PersistenceUtil import PersistenceUtil




class MultiSensorAdaptor(threading.Thread):
    '''
    classdocs
    '''
    rateInSec = 10
    enableTempSensor = False
    enableHumidSensor = False
    tempSensorData = SensorData()
    humidSensorData = SensorData()
    hi2cSensorData = SensorData()
    manager = SensorDataManager()
    tempsensor = TempSensorAdaptorTask()
#     humiditysensor = HumiditySensorAdaptorTask()
#     hi2csensor = HI2CSensorAdaptorTask()
    persistenceutil = PersistenceUtil()
    
    
    


    def __init__(self, rateInSec=10):
        threading.Thread.__init__(self)
        #self.sensorData = SensorData()
        self.rateInSec = rateInSec
        #self.time      = self.sensorData.timeStamp 

    def run(self):
        while True:
            
            
            
            if self.enableTempSensor:
                self.tempSensorData.setName('Temp')
                self.tempSensorData.addValue(self.tempsensor.getTemperature())
                #print(self.sensorData.curValue)
                #self.manager.handleSensorData(self.sensorData)       
                self.persistenceutil.writeSensorDataToRedis(self.tempSensorData)      
                sleep(self.rateInSec)   
            
            if self.enableHumidSensor:
                self.humidSensorData.setName("Humid")                
                self.humidSensorData.addValue(self.humiditysensor.getHumidity())
                #print(str(datetime.now()) + "SenseHat API Humidity   " + str(self.curHumid))
                #print(str(datetime.now()) + "I2C Direct Humidity:    " + str(self.i2cHumid.getHumidityData()))
                #print(self.sensorData.curValue)
                #self.manager.handleSensorData(self.sensorData)
                self.persistenceutil.writeSensorDataToRedis(self.humidSensorData)
                
                sleep(self.rateInSec)
                
            if self.enableHI2CSensor:
#                 self.displayAccelerometerData()
#                 self.displayMagnetometerData()
#                 self.displayPressureData()
#                 self.displayHumidityData()
#                 self.getHumidityData()
#                 print(str(datetime.now()) + "I2C Direct Humidity:    " + str(self.RH))
                self.hi2cSensorData.setName("I2C_Humid")
                self.hi2cSensorData.addValue(self.hi2csensor.getHumidityData())
                #self.manager.handleSensorData(self.sensorData)
                self.persistenceutil.writeSensorDataToRedis(self.hi2cSensorData)
                
                sleep(self.rateInSec)    
            