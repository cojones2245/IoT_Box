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


def write_msg_file(msg):
    with open('status.txt', 'w') as f:
        f.write(msg)
        # f.write('\n')


def read_status_file():
    with open('status.txt') as f:
        lines = f.readlines()
        status = lines[0]
    return str(status)


def check_against_file():
    status = str(asyncio.run(plug_status()))
    if read_status_file() != status:
        write_msg_file(status)
        return True
    return False


def watch_file_change():
    status1 = read_status_file()
    while True:
        status2 = read_status_file()
        if status1 != status2:
            run()
            status1 = status2
        if check_against_file():
            run()
            status1 = read_status_file()
        time.sleep(3)


# make a new thread that watches the text file
# while True:
# check file

def run():
    mqttBroker = "199.244.104.202"
    client = mqtt.Client("Front")
    client.username_pw_set(username="dave", password="password")
    client.connect(mqttBroker)
    power_status = asyncio.run(plug_status())
    client.publish("vmi/box1/plug1/status", power_status)
    print("Just published " + str(power_status) + " to Topic vmi/box1/#")
    time.sleep(2)
    client.disconnect()


# Database
# Query all items for a box - will recieve all attributes
# Keep a local file on the pi and the

watch_file_change()
