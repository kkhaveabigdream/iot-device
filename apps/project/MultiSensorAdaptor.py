'''
Created on Feb 5, 2020

@author: sk199
'''
from time import sleep
import threading
from labs.common.SensorData import SensorData
#from project.SensorDataManager import SensorDataManager
from project.TempSensorAdaptorTask import TempSensorAdaptorTask
from project.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
# from labs.module06.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask
from labs.common.PersistenceUtil import PersistenceUtil
from project.CoapClientConnector import CoapClientConnector
from labs.common.DataUtil import DataUtil





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
    #manager = SensorDataManager()
    tempsensor = TempSensorAdaptorTask()
    humiditysensor = HumiditySensorAdaptorTask()
#     hi2csensor = HI2CSensorAdaptorTask()
    persistenceutil = PersistenceUtil()
    coapClientConnector = CoapClientConnector();
    dataUtil = DataUtil();
    
    
    


    def __init__(self, rateInSec=10):
        threading.Thread.__init__(self)
        #self.sensorData = SensorData()
        self.rateInSec = rateInSec
        #self.time      = self.sensorData.timeStamp 

    def run(self):
        while True:
            
            
            
            if self.enableTempSensor:

                resource = 'temp';
                self.tempSensorData.setName('Temp')
                self.tempSensorData.addValue(self.tempsensor.getTemperature())
                #print(self.sensorData.curValue)
                #self.manager.handleSensorData(self.sensorData)       
                #self.persistenceutil.writeSensorDataToRedis(self.tempSensorData) 
                payload = self.dataUtil.toJsonFromSensorData(self.tempSensorData)
                #print(payload)
                self.coapClientConnector.postRequest(resource, payload)
                sleep(5)
                  
                self.coapClientConnector.getRequest(resource)   
                sleep(5)   
             
            if self.enableHumidSensor:
                resource = 'soilMoisture';
                self.humidSensorData.setName("SoilMoisture")                
                self.humidSensorData.addValue(self.humiditysensor.getHumidity())
                #print(str(datetime.now()) + "SenseHat API Humidity   " + str(self.curHumid))
                #print(str(datetime.now()) + "I2C Direct Humidity:    " + str(self.i2cHumid.getHumidityData()))
                #print(self.sensorData.curValue)
                #self.manager.handleSensorData(self.sensorData)
                payload = self.dataUtil.toJsonFromSensorData( self.humidSensorData)
                #print(payload)
                self.coapClientConnector.postRequest(resource, payload)
                sleep(5)
                  
                self.coapClientConnector.getRequest(resource)   
                sleep(5)   
            