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
        
        
    
    def run(self,temp):
        self.sh.show_letter("H")
        #self.sh.show_letter("H",self.red)
        sleep(1)
        self.msg = str(temp) + chr(223)
        self.sh.show_message(self.msg)
        #self.sh.show_message(temp+ u'\u2103',scroll_speed=0.5)
        
    def run2(self,temp):
        self.sh.show_letter("C")
        #self.sh.show_letter("C",self.blue)
        sleep(1)
        self.msg = str(temp) + chr(223)
        self.sh.show_message(self.msg)
        #self.sh.show_message(temp + u'\u2103',scroll_speed=0.5)