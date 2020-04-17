'''
Created on Apr 16, 2020

@author: sk199
'''

import spidev
from time import sleep

class mcp3008(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        spi = spidev.SpiDev()
        spi.open(0,0)

    def getAdc (self,channel):
        if ((channel>7)or(channel<0)):        
            return -1
 
        r = spi.xfer([1, (8+channel) << 4, 0])       
        adcOut = ((r[1]&3) << 8) + r[2]       
        percent = int(round(adcOut/10.24))   
        print("ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent))
        return percent

