import pika
import time
import requests
import math
import random


TOKEN = "BBFF-lUiRoKkbCIgg0issBVPuvnkUUPLWGo"  # Put your TOKEN here
DEVICE_LABEL = "machine2"  # Put your device label here 
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here
connection = pika.BlockingConnection(pika.ConnectionParameters('3.220.79.140', 5672, '/', pika.PlainCredentials("user", "password")))
channel = connection.channel()
datos =[]
def callback(ch, method, properties, body):
    print(f'{body} is received')
    a=body.decode()
    datos.append(a)
    i = 0
    while (len(datos)-1 > i ):
        main(i)
        time.sleep(1)
        i = i + 1
    

def build_payload(variable_1, datos, indexValue):
    # Creates two random values for sending data
    value_1 = datos[indexValue]
    print(value_1)
    payload = {variable_1: value_1}

    return payload

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def main(indexValue):
    payload = build_payload(
        VARIABLE_LABEL_1, datos, indexValue)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()



