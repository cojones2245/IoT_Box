import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import asyncio
from kasa import SmartPlug


async def plug_status(ip):
    # Create smart plug
    p = SmartPlug("192.168.8.101")
    await p.update()

    return p.is_on


def run():
    mqttBroker = "199.244.104.202"
    client = mqtt.Client("Front")
    client.username_pw_set(username="dave", password="password")
    client.connect(mqttBroker)

    while True:
        power_status = asyncio.run(plug_status())
        client.publish("test", power_status)
        print("Just published " + str(power_status) + " to Topic test")
        time.sleep(5)

#Database
#Query all items for a box - will recieve all attributes
#Keep a local file on the pi and the