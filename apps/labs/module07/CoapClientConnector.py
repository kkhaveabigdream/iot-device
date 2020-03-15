'''
Created on Mar 11, 2020

@author: sk199
'''
from coapthon.client.helperclient import HelperClient
import logging


class CoapClientConnector(object):
    '''
    classdocs
    '''    

    def __init__(self):
        '''
        Constructor
        '''
             
    def initClient(self):
        host = "127.0.0.1"
        port = 5683
        self.client = HelperClient(server=(host,port))
         
    def getRequest(self,resource):
        self.initClient()       
        response = self.client.get(resource)
        print('------->')
        print("Starting Get Request...\n")
        logging.info(response.pretty_print())
        logging.info(response.payload)
        #print(response.payload)  
        print('------->')
        self.client.stop()
        
    def postRequest(self,resource,payload):
        self.initClient()   
        response = self.client.post(resource,payload)
        print('------->')
        #print(response.pretty_print()) 
        print("Starting Post Request...\n")
        logging.info(response.pretty_print())
        print('------->')
        
        self.client.stop()
        
    def putRequest(self,resource,payload):
        self.initClient()   
        response = self.client.put(resource,payload)
        print('------->')
        #print(response.pretty_print()) 
        print("Starting Put Request...\n")
        logging.info(response.pretty_print())
        print('------->')
        
    def deleteRequest(self,resource):    
        self.initClient()   
        response = self.client.delete(resource)
        print('------->')
        print("Starting Delete Request...\n")
        print('------->')
        self.client.stop()