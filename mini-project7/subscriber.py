import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

broker = "test.mosquitto.org"
port = 1883
topic = "ecrio/demo/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)

client.loop_forever()