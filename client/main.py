import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import asyncio
from kasa import SmartPlug

mqttBroker = "10.10.10.121"
client = mqtt.Client("Power_Box1")
client.connect(mqttBroker)


async def plug_status():
    # Create smart plug
    p = SmartPlug("192.168.10.101")
    await p.update()

    return p.is_on


while True:
    power_status = asyncio.run(plug_status())
    client.publish("Plug Status: ", power_status)
    print("Just published " + str(power_status) + " to Topic POWER")
    time.sleep(5)
