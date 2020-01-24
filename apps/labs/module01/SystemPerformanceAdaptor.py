'''
Created on Jan 20, 2020

@author: sk199
'''
import psutil
import logging
from time import sleep
from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
import threading
from labs.module01.SystemMemUtilTask import SystemMemUtilTask

class SystemPerformanceAdaptor(threading.Thread):
    '''
    classdocs
    '''

    enableAdaptor = False
    rateInSec = 5

    def __init__(self, rateInSec=5):
        #threading.Thread.__init__(self)
        super(SystemPerformanceAdaptor,self).__init__()
        self.rateInSec=rateInSec

    
    def run(self):
        while True:
            if self.enableAdaptor:
                #cpuUtil = SystemCpuUtilTask.getDataFromSensor()
                c = SystemCpuUtilTask()
                cpuUtil = c.getDataFromSensor()
                m = SystemMemUtilTask()
                memUtil = m.getDataFromSensor()
                perfData1 = 'CPU Utilization=' + str(cpuUtil) 
                perfData2 ='Memory Utilization=' +str(memUtil)
                
                logging.info(perfData1)
                logging.info(perfData2)
                sleep(self.rateInSec)

