'''
Created on Mar 11, 2020

@author: sk199
'''
from coapthon.client.helperclient import HelperClient
from labs.common.ActuatorData import ActuatorData
import logging
from project.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.common.DataUtil import DataUtil


class CoapClientConnector(object):
    '''
    classdocs
    '''   


    def __init__(self):
        '''
        Constructor
        '''
        
    '''
    Connect to the local Coap Server
    '''           
    def initClient(self):
        #host = "127.0.0.1"
        #host = "169.254.94.97"
        host = "192.168.0.131"
        port = 5683
        self.client = HelperClient(server=(host,port))
        #self.actuatorData = ActuatorData()
        self.multiActuator = MultiActuatorAdaptor()
        self.dataUtil = DataUtil()
    
    '''
    Get the payload from resource
    '''     
    def getRequest(self,resource):
        self.initClient()       
        response = self.client.get(resource)
        print('------->')
        print("Starting Get Request...\n")
        logging.info(response.pretty_print())
        logging.info(response.payload)
        self.actuatorData = self.dataUtil.toActuatorDataFromJson2(response.payload)
        print(response.payload)
        self.actuatorData.setCommand(self.actuatorData.Value)
        self.multiActuator.updateActuator(self.actuatorData)
        #print(response.payload)  
        print('------->')
        self.client.stop()
     
    '''
    Post the data to the resource
    '''   
    def postRequest(self,resource,payload):
        self.initClient()   
        response = self.client.post(resource,payload)
        print('------->')
        #print(response.pretty_print()) 
        print("Starting Post Request...\n")
        logging.info(response.pretty_print())
        print('------->')
        
        self.client.stop()
    
    '''
    Update the resource
    '''    
    def putRequest(self,resource,payload):
        self.initClient()   
        response = self.client.put(resource,payload)
        print('------->')
        #print(response.pretty_print()) 
        print("Starting Put Request...\n")
        logging.info(response.pretty_print())
        print('------->')
    
    '''
    Delete the resource
    '''   
    def deleteRequest(self,resource):    
        self.initClient()   
        response = self.client.delete(resource)
        print('------->')
        print("Starting Delete Request...\n")
        print('------->')
        self.client.stop()