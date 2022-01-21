import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import asyncio
from kasa import SmartPlug

global_change = False


def on_message(client, userdata, message):
    global global_change
    sub_msg = str(message.payload.decode("utf-8"))
    print("Received message: ", sub_msg)
    if sub_msg == "on":
        global_change = True
    else:
        global_change = False
    asyncio.run(main())


mqttBroker = "199.244.104.202"
client = mqtt.Client("Front")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("test")
client.on_message = on_message
time.sleep(30)
client.loop_end()


async def main():
    p = SmartPlug("192.168.10.101")

    await p.update()
    print(p.alias)
    if global_change:
        await p.turn_on()
    else:
        await p.turn_off()


# if __name__ == "__main__":
#     asyncio.run(main())
