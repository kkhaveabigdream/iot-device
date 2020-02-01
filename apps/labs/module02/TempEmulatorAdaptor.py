'''
Created on Jan 28, 2020

@author: sk199
'''
import logging
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
from time import sleep

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
logging.info("Starting temperature emulator adaptor  daemon thread...")

tempsensoremulator = TempSensorEmulatorTask()
tempsensoremulator.daemon = True
tempsensoremulator.enableEmulator = True
tempsensoremulator.start()

while (True):
    sleep(10)
    pass
