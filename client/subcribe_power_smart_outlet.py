import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import asyncio
from kasa import SmartPlug


async def smart_outlet(state):
    p = SmartPlug("192.168.8.101")

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


def on_message(client, userdata, message):
    sub_msg = str(message.payload.decode("utf-8"))
    print("Received message: ", sub_msg)

    asyncio.run(smart_outlet(sub_msg))


mqttBroker = "199.244.104.202"
client = mqtt.Client("Front")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("test")
client.on_message = on_message

time.sleep(30)
client.loop_stop()
client.disconnect()
