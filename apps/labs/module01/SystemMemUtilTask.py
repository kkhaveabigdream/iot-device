'''
Created on Jan 20, 2020

@author: sk199
'''
import psutil


class SystemMemUtilTask(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def getDataFromSensor(self):
        memUtil = psutil.virtual_memory().percent
        return(memUtil)