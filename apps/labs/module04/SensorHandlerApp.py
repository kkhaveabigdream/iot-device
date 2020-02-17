'''
Created on Feb 5, 2020

@author: sk199
'''
import logging
from time import sleep
from labs.module04.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module04.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
from labs.module04.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask
from _datetime import datetime


logging.getLogger().setLevel(logging.INFO)
#logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
logging.info("Starting temperature sensor adaptor  daemon thread...")


tempsensoradaptor = TempSensorAdaptorTask()
tempsensoradaptor.daemon                = False
tempsensoradaptor.enableTempSensor        = False
tempsensoradaptor.start()
humiditysensoradaptor = HumiditySensorAdaptorTask()
humiditysensoradaptor.enableHumidSensor = True
humiditysensoradaptor.start()
hi2csensoradaptor = HI2CSensorAdaptorTask()
hi2csensoradaptor.enableHI2CSensor      = True
hi2csensoradaptor.start()


while (True):
    sleep(1)
    sh  = humiditysensoradaptor.curHumid
    i2c = hi2csensoradaptor.RH    
    print(str(datetime.now()) + "    SenseHat API Humidity:  " + str(sh))
    print(str(datetime.now()) + "    I2C Direct Humidity:    " + str(i2c))
    print(str(datetime.now()) + "    Difference:             " + str((abs(sh-i2c))/sh*100) + "%")
    print('--------------------------------------------------------    ')
    sleep(10)
    pass
    