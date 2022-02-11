import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import asyncio
from kasa import SmartPlug


async def plug_status():
    # Create smart plug
    p = SmartPlug("192.168.8.101")
    await p.update()

    return p.is_on


def check_file():
    with open('status.txt') as f:
        lines = f.readlines()
        line = lines[0]
    status = str(asyncio.run(plug_status()))
    print(status)
    if str(line) != status:
        run()

#make a new thread that watches the text file

def run():
    mqttBroker = "199.244.104.202"
    client = mqtt.Client("Front")
    client.username_pw_set(username="dave", password="password")
    client.connect(mqttBroker)
    power_status = asyncio.run(plug_status())
    client.publish("vmi/box1/plug1", power_status)
    print("Just published " + str(power_status) + " to Topic vmi/box1/#")
    time.sleep(2)
    client.disconnect()

# Database
# Query all items for a box - will recieve all attributes
# Keep a local file on the pi and the
