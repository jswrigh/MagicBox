#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import atexit
import datetime
import automationhat #Pimoroni library for PiHat
import boto3 # AWS Python library
import requests # Open source library for Json requests
import json
import pyowm # Open source library for accessing openweathermap.org data
import DHT22
import pigpio
import Sensor
import tkinter as tk

from MagicBoxController import MagicBoxController

def main():
    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='HomeLink')

    # Verify connection and display attributes
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))
    print(queue.attributes.get('SentTimestamp'))

    # Setup connection to Nature Remo
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer oh1PJgWskEMq4Km95GRvC_iJvtrMbL8RQJCObPwqKt8.XAg_MhK8zwOFqIueYYPFotfZ8xTOEWAdNv3ZHDRsQkY',
    }

    # Setup connection to openweathermap to get outdoor temperature
    #owm = pyowm.OWM('123e236852641b9b3bfd755ffa553566')  # You MUST provide a valid API key
    #observation = owm.weather_at_id(4752031)
    #w = observation.get_weather()
    #print(w.get_wind())
    #print(w.get_humidity())
    #print(w.get_temperature('fahrenheit'))

    # Setup connection to internal DHT22 temperature probe
    # Intervals of about 2 seconds or less will eventually hang the DHT22.
    INTERVAL=600

    pi = pigpio.pi()
    s = DHT22.sensor(pi, 4)
    r = 0
    adjustment = -3.7 # Adjust temperature reading
    next_reading = time.time()

    controller = MagicBoxController()

    # Build Gui and start it
    root = tk.Tk()
    root.title('Main Application')

    controller.init_view(root)


    print ('Bye Bye')



if __name__ == "__main__":
    main()
