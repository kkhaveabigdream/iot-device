'''
Created on Feb 5, 2020

@author: sk199
'''
from sense_hat import SenseHat
import threading
from time import sleep

class SenseHatLedActivator(threading.Thread):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.sh = SenseHat()
        self.red = (255,0,0)
        self.blue = (0,0,255)
        
    '''
    If current temperature exceeds the 'nominalTemp, a red letter 'H' representing 'Hot' will show on the LED for 1 second, 
    If current temperature falls below the 'nominalTemp, a blue letter 'C' representing 'Cool' will show on the LED for 1 second,
    After that, the LED will show current Temperature value    
    '''    
    
    def run(self,temp):
        self.sh.show_letter("H")
        #self.sh.show_letter("H",self.red)
        sleep(1)
        self.msg = str(temp) + ' ' + chr(176) + 'C'
        self.sh.show_message(self.msg)
        #self.sh.show_message(self.msg,scroll_speed=0.3)
        
    def run2(self,temp):
        self.sh.show_letter("C")
        #self.sh.show_letter("C",self.blue)
        sleep(1)
        self.msg = str(temp)+ ' ' + chr(176) + ' C'
        self.sh.show_message(self.msg)
        #self.sh.show_message(self.msg,scroll_speed=0.3)