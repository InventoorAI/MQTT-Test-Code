import paho.mqtt.client as mqtt
import json
import time

# ThingsBoard host and port
THINGSBOARD_HOST = 'demo.thingsboard.io'
THINGSBOARD_PORT = 1883

# Access token for the device
ACCESS_TOKEN = '1oJEbmZamsMk09N4CIaT'

# Payload data
payload = {
    "status": "B"
}

# Convert the payload to JSON
payload_json = json.dumps(payload)

# Define the callback function for connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Define the callback function for message publishing
def on_publish(client, userdata, mid):
    print("Message published")

# Create an MQTT client instance
client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Assign the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to ThingsBoard MQTT broker
client.connect(THINGSBOARD_HOST, THINGSBOARD_PORT, 60)

# Start the MQTT loop
client.loop_start()

# Publish data every second
try:
    while True:
        client.publish('v1/devices/me/telemetry', payload_json)
        time.sleep(1)  # Wait for 1 second before publishing again
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
