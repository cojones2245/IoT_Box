import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import asyncio
from kasa import SmartPlug

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Power_Box1")
client.connect(mqttBroker)

#
#
# # async def main():
# #     # Create smart plug
# #     p = SmartPlug("192.168.10.11")
# #     await p.update()
#

while True:
    power_status = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", power_status)
    print("Just published " + str(power_status) + " to Topic TEMPERATURE")
    time.sleep(1)
