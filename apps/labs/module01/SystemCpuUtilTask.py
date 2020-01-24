'''
Created on Jan 20, 2020

@author: sk199
'''
import psutil


class SystemCpuUtilTask():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''


    def getDataFromSensor(self):
        cpuUtil = psutil.cpu_percent(0.1, False)
        return(cpuUtil)

#print(SystemCpuUtilTask.getDataFromSensor())
