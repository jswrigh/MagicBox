import json
import requests
import pyowm # Open source library for accessing openweathermap.org data
from MagicBoxDHT22 import MagicBoxDHT22

class MagicBoxQueue(object):

    def __init__(self):
        self.data = {}  
        self.data['environment'] = {  
            'insideTemp': '600',
            'outsideTemp': '500',
            'insideHumidity': '300'
        }
        self.data['settings'] = {  
            'setTemp': '700',
            'iFeel': '-5',
        }
        self.dht22=MagicBoxDHT22()
        print(self.dht22.tempF)

        # Setup connection to openweathermap to get outdoor temperature
        owm = pyowm.OWM('123e236852641b9b3bfd755ffa553566')  # You MUST provide a valid API key
        self.observation = owm.weather_at_id(4752031)
        w = self.observation.get_weather()
        print('OpenWeather Data: ')
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('fahrenheit'))


    def writeQ(self):
        print(self.data)
        with open('data.txt', 'w') as outfile:  
            json.dump(self.data, outfile)

    def readQ(self):
        with open('data.txt') as json_file:  
            data = json.load(json_file)
            print(data)

    def updateInsideTemp(self):
        self.dht22.DHT22()
        nowTemp = self.dht22.tempF
        self.data['environment']['insideTemp'] = nowTemp
        self.writeQ()
        return(nowTemp)
        
    def updateInsideHumidity(self):
        self.dht22.DHT22()
        nowHumidity = self.dht22.humidity
        self.data['environment']['insideHumidity'] = nowHumidity
        self.writeQ()
        return(nowHumidity)

    def updateOutsideTemp(self):
        nowWeather = self.observation.get_weather()
        nowExtTemp = nowWeather.get_temperature('fahrenheit')['temp']
        self.data['environment']['outsideTemp'] = nowExtTemp
        self.writeQ()
        return(nowExtTemp)

        