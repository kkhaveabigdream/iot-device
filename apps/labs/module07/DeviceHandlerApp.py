'''
Created on Mar 11, 2020

@author: sk199
'''
from labs.module07.CoapClientConnector import CoapClientConnector
from labs.common.SensorData import SensorData
from labs.module07.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.common.DataUtil import DataUtil
import logging


if __name__ == '__main__':
    resource = 'temp'
    #payload = "for test"

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
    print('------->')
    logging.info("Connecting to Coap Server...")
    coapClientConnector = CoapClientConnector()
    tempSensorData = SensorData()
    temp = TempSensorAdaptorTask()
    dataUtil = DataUtil()
    
    tempSensorData.addValue(temp.getTemperature())  
    payload = dataUtil.toJsonFromSensorData(tempSensorData)
    print("Json Before issuing the request...")
    logging.info(payload)
    print('------->') 
    coapClientConnector.postRequest(resource, payload)
    coapClientConnector.putRequest(resource, payload)
    coapClientConnector.getRequest(resource)
    coapClientConnector.deleteRequest(resource)
    