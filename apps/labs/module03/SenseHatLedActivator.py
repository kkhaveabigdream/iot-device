'''
Created on Feb 5, 2020

@author: sk199
'''
from sense_hat import SenseHat


class SenseHatLedActivator(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.sh = SenseHat
        
    
    def run(self):
        self.sh.show_letter("H")
        
    def run2(self):
        self.sh.show_letter("C")