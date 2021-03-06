'''
Created on Jan 20, 2020

@author: sk199
'''
import logging
import threading
from time import sleep

import psutil

from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
from labs.module01.SystemMemUtilTask import SystemMemUtilTask


class SystemPerformanceAdaptor(threading.Thread):
    '''
    classdocs
    '''

#set rate to retrieve getDataFromSensor() every 5 second.
    enableAdaptor = False
    rateInSec = 5

#constructor
    def __init__(self, rateInSec=5):
        #threading.Thread.__init__(self)
        super(SystemPerformanceAdaptor,self).__init__()
        self.rateInSec=rateInSec

 
#Displaying the output from SystemCpuUtilTask and SystemMemUtilTask 
#Using log message to output the CPU Utilization and Memory Utilization
 
    def run(self):
        while True:
            if self.enableAdaptor:
                c = SystemCpuUtilTask()
                cpuUtil = c.getDataFromSensor()
                m = SystemMemUtilTask()
                memUtil = m.getDataFromSensor()
                perfData1 = 'CPU Utilization=' + str(cpuUtil) 
                perfData2 ='Memory Utilization=' +str(memUtil)
                
                logging.info(perfData1)
                logging.info(perfData2)
                sleep(self.rateInSec)

