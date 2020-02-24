'''
Created on Feb 5, 2020 

@author: sk199
'''
import logging
from time import sleep
from labs.module05.MultiSensorAdaptor import MultiSensorAdaptor


from labs.common.ActuatorDataListener import ActuatorDataListener



#from labs.common.SensorDataListener import SensorDataListener


logging.getLogger().setLevel(logging.INFO)
#logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
logging.info("Starting temperature sensor adaptor  daemon thread...")




multisensoradaptor = MultiSensorAdaptor()
multisensoradaptor.enableTempSensor        = True
multisensoradaptor.enableHumidSensor = False
multisensoradaptor.enableHI2CSensor      = False
multisensoradaptor.start()
#sensordatalistener = SensorDataListener()
actuatordatalistener = ActuatorDataListener()


while (True):  
    #sensordatalistener.listener() 
    actuatordatalistener.listener()
    sleep(10)
    pass
    