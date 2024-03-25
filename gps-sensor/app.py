from counterfit_connection import CounterFitConnection
CounterFitConnection.init()

import time
import counterfit_shims_serial
import pynmea2
import json
from azure.iot.device import IoTHubDeviceClient, Message
import os

serial = counterfit_shims_serial.Serial('/dev/ttyAMA0')

CONNECTION_STRING = os.getenv("CONNECTION_STRING")

device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
print("Connected to Azure IoT Hub")

def send_gps_data(line):
    msg = pynmea2.parse(line)
    if msg.sentence_type == 'GGA':
        # print(f'Latitude: {msg.lat} Longitude: {msg.lon} Altitude: {msg.altitude} Time: {msg.timestamp}')
        lat = pynmea2.dm_to_sd(msg.lat)
        lon = pynmea2.dm_to_sd(msg.lon)

        if msg.lat_dir == 'S':
            lat = -lat

        if msg.lon_dir == 'W':
            lon = -lon

        msg_json = {"gps": {"lat": lat, "lon":lon}}
        print(f'Sending message: {msg_json}')
        message = Message(json.dumps(msg_json))
        device_client.send_message(message)

        # print(f'Latitude: {lat}, {lon} - from {msg.num_sats} satellites at {msg.timestamp}')

while True:
    line = serial.readline().decode('utf-8')
    
    while len(line) > 0:
        send_gps_data(line)
        line = serial.readline().decode('utf-8')
        
        time.sleep(60)
