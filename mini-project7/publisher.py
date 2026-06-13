import paho.mqtt.client as mqtt
import time
import random

broker = "test.mosquitto.org"   # public MQTT broker
port = 1883
topic = "ecrio/demo/topic"

client = mqtt.Client()
client.connect(broker, port)

while True:
    message = f"Random number: {random.randint(1,100)}"
    client.publish(topic, message)
    print("Published:", message)
    time.sleep(2)