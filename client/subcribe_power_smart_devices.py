from queue import Queue
import paho.mqtt.client as mqtt
import time
import asyncio
import json
from kasa import SmartDevice, SmartPlug


async def plug_status():
    # Create smart plug
    p = SmartPlug("192.168.8.101")
    await p.update()

    return p.is_on


async def smart_device(state):
    p = SmartPlug("192.168.8.101")

    await p.update()
    print(p.alias)
    if state == "True":
        await p.turn_on()
    else:
        await p.turn_off()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=", rc)
    else:
        print("Bad connection Returned code=", rc)
    client.subscribe("vmi/box1/#")


# def convert_JSON(message):
#     conv = json.loads(message)
#     # boxId = conv['boxId']
#     # equipmentId = conv['equipmentId']
#     msg = conv['message']
#     ## this is where we run the queries to get the boxname and equipment ip


def on_message(client, userdata, message):
    sub_msg = str(message.payload.decode("utf-8"))
    print("Received message: ", sub_msg)
    # ip = db.get_device_ip()
    #
    # Query device ip
    asyncio.run(smart_device(sub_msg))
    write_msg_file(sub_msg)


def write_msg_file(msg):
    with open('status.txt', 'w') as f:
        f.write(msg)
        # f.write('\n')


def check_device(msg):
    if msg == str(plug_status()):
        return False
    else:
        return True


def run():
    while True:
        mqttBroker = "199.244.104.202"
        client = mqtt.Client("Front")
        client.on_connect = on_connect
        client.username_pw_set(username="dave", password="password")
        client.connect(mqttBroker)
        client.loop_start()
        client.on_message = on_message
        time.sleep(45)
        client.loop_stop()
    client.disconnect()


run()
