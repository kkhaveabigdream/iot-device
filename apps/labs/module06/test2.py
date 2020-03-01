'''
Created on Feb 28, 2020

@author: sk199
'''
import paho.mqtt.client as mqtt  
import time  
  
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code "+str(rc))  
    #client.subscribe("test")
  
def on_message(client, userdata, msg):  
    print(msg.topic+" "+str(msg.payload))  
  
client = mqtt.Client()  
client.on_connect = on_connect  
client.on_message = on_message  
client.connect("mqtt.eclipse.org", 1883)  
client.subscribe("test")
client.loop_forever()
  
# while client.loop() == 0:  
#     msg = "test message from Publisher "+time.ctime()  
#     client.publish("test/rensanning/time", msg, 0, True)  
#     print("message published")  
#     time.sleep(1.5)  
#     pass  