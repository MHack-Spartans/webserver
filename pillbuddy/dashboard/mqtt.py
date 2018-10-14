import paho.mqtt.client as paho
import ssl
import json

import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

def on_connect(client, userdata, flags, rc):
    print("Connection returned result:", rc)

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

def publish_dispense_now(slot, number):
    msg = {
        "slot": slot,
        "number": number,
    }
    mqttc.publish("dispense/now", payload=json.dumps(msg), qos=0)

def publish_buzzer():
    msg = { "buzzer": True }
    mqttc.publish("dispense/buzzer", payload=json.dumps(msg), qos=0)

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "data.iot.us-east-1.amazonaws.com"
awsport = 8883
clientId = "PillBuddyWebserver"
thingName = "PillBuddyWebserver"
caPath = os.path.join(BASE, "certs/aws-iot-rootCA.crt")
certPath = os.path.join(BASE, "certs/certificate.pem.crt")
keyPath = os.path.join(BASE, "certs/private.pem.key")

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.subscribe("dispense/#")

# mqttc.loop_start() # moved to __init__.py