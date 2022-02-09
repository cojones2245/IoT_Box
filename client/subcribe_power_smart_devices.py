import paho.mqtt.client as mqtt
import time
import asyncio
import db
import json
from kasa import SmartDevice


async def smart_device(state, smart_device_ip):
    p = SmartDevice(smart_device_ip)

    await p.update()
    print(p.alias)
    if state == "on":
        await p.turn_on()
    else:
        await p.turn_off()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=", rc)
    else:
        print("Bad connection Returned code=", rc)


# def convert_JSON(message):
#     conv = json.loads(message)
#     # boxId = conv['boxId']
#     # equipmentId = conv['equipmentId']
#     msg = conv['message']
#     ## this is where we run the queries to get the boxname and equipment ip


def on_message(client, userdata, message):
    sub_msg = str(message.payload.decode("utf-8"))
    print("Received message: ", sub_msg)
    ip = db.get_device_ip()
    asyncio.run(smart_device(sub_msg, ip))


def run():
    mqttBroker = "199.244.104.202"
    client = mqtt.Client("Front")
    client.on_connect = on_connect
    client.username_pw_set(username="dave", password="password")
    client.connect(mqttBroker)
    client.loop_start()
    client.subscribe("vmi/box1/#")
    #Find some way to pass the topic to the db code
    #find out how to get the sub topic from the paho documentation
    client.on_message = on_message
    topic =
     #need multi threading
    time.sleep(30)
    client.loop_stop()
    client.disconnect()

    #
