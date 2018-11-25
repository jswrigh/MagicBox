import json
import requests
import pyowm # Open source library for accessing openweathermap.org data
from MagicBoxDHT22 import MagicBoxDHT22

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer oh1PJgWskEMq4Km95GRvC_iJvtrMbL8RQJCObPwqKt8.XAg_MhK8zwOFqIueYYPFotfZ8xTOEWAdNv3ZHDRsQkY',
}

class MagicBoxQueue(object):

    def __init__(self):
        self.data = {}  
        self.data['environment'] = {  
            'insideTemp': '600',
            'outsideTemp': '500',
            'insideHumidity': '300',
            'outsideHumidity': '100',
            'Sandi Living Roomte': '450',
            'Sandi Living Roomhu' : '550',
            'Sandi Living Roomil': '350',
            'Sandi Bedroomte': '450',
            'Sandi Bedroomhu': '550',
            'Sandi Bedroomil': '350',
            'Balsamte': '450',
            'Balsamhu': '550',
            'Balsamil': '350',
        }
        self.data['settings'] = {  
            'setTemp': '700',
            'iFeel': '-5',
        }
        self.data['status'] = {
            'gasRelay': 'OFF',
            'lrRemoCommand': 'H72',
            'brRemoCommand': 'H70',
            'bwRemoCommand': 'H68'
        }
        self.data['signals'] = {
            'Sandi Living Room': {},'LG Bedroom': {},'LG Family Room': {},'TV': {},
                    'Family Room AC': {}
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

    def getInsideTemp(self):
        self.readQ()
        return(self.data['environment']['insideTemp'])

    def setInsideTemp(self, nowTemp):
        self.data['environment']['insideTemp'] = nowTemp
        self.writeQ()
        
    def updateInsideRh(self):
        self.dht22.DHT22()
        nowHumidity = self.dht22.humidity
        self.data['environment']['insideHumidity'] = nowHumidity
        self.writeQ()
        return(nowHumidity)

    def getInsideRh(self):
        self.readQ()
        return(self.data['environment']['insideHumidity'])

    def setInsideRh(self, nowRh):
        self.data['environment']['insideHumidity'] = nowRh
        self.writeQ()
        
    def updateOutsideTemp(self):
        nowWeather = self.observation.get_weather()
        nowExtTemp = nowWeather.get_temperature('fahrenheit')['temp']
        self.data['environment']['outsideTemp'] = nowExtTemp
        self.writeQ()
        return(nowExtTemp)
    
    def getOutsideTemp(self):
        self.readQ()
        return(self.data['environment']['outsideTemp'])

    def setOutsideTemp(self, nowTemp):
        self.data['environment']['outsideTemp'] = nowTemp
        self.writeQ()
        
    def updateOutsideRh(self):
        nowWeather = self.observation.get_weather()
        nowExtRh = nowWeather.get_humidity()
        self.data['environment']['outsideHumidity'] = nowExtRh
        self.writeQ()
        return(nowExtRh)
    
    def getOutsideRh(self):
        self.readQ()
        return(self.data['environment']['outsideHumidity'])

    def setOutsideRh(self, nowRh):
        self.data['environment']['outsideHumidity'] = nowRh
        self.writeQ()

    def updateRemoData(self, remoID, type):
        response = requests.get('https://api.nature.global/1/devices', headers=headers)
        remData = response.json()
        print (json.dumps(remData, indent=4, separators=(',', ': '), sort_keys=True))
        print (len(remData))
        for x in range (0,len(remData)):
            print (x)
            if remData[x]['name'] == remoID:
                print ("name: " + remData[x]['name'])
                if type == 'te':
                    celsius = float (remData[x]['newest_events'][type]['val'])
                    fahrenheit = 9.0/5.0 * celsius + 32
                    print(fahrenheit)
                    print(round(fahrenheit,1))
                    print(remoID+type)
                    self.data['environment'][remoID+type] = round(fahrenheit,1)
                    self.writeQ()
                    return(round(fahrenheit,1))
                else:
                    self.data['environment'][remoID+type] = remData[x]['newest_events'][type]['val']
                    self.writeQ()
                    return(remData[x]['newest_events'][type]['val'])

    def updateRemoSignals(self):
        response = requests.get('https://api.nature.global/1/appliances', headers=headers)
        remData = response.json()
        print (json.dumps(remData, indent=4, separators=(',', ': '), sort_keys=True))
        print (len(remData))
        for x in range (0,len(remData)):
            nickname = remData[x]['nickname']
            print ("nickname: " + nickname)
#            print(self.data['signals'])
#            self.data['signals']['nickname'] = remData[x]['nickname']#['signals']
            print("---------")
            for y in range(0,len(remData[x]['signals'])):
                signalName=remData[x]['signals'][y]['name']
                signalId=remData[x]['signals'][y]['id']
                print(signalName + " : " + signalId)
#                self.data['signals'][nickname][signalName]['id']=signalId
                self.data['signals'][nickname][signalName]=signalId
#        print(self.data['signals'])
        
    def getRemoOptions(self, nickname):
        print("XXXXXXXXXX")
        print(self.data['signals'][nickname])
        print(self.data['signals'][nickname].keys())
        codenames = list(self.data['signals'][nickname].keys())
        for x in range (0, len(codenames)):
            print(codenames[x])
        return(codenames)
    
    def getRemoData(self, remoID, type):
        self.readQ()
        return(self.data['environment'][remoID+type])

    def setRemoData(self, remoID, type, envData):
        self.data['environment'][remoID+type] = envData
        self.writeQ()
        
    def getGasRelay(self):
        self.readQ()
        return(self.data['status']['gasRelay'])

    def setGasRelay(self, gr):
        self.data['status']['gasRelay'] = gr
        self.writeQ()
    
    def getLastRemoCmd(self, remoID):
        self.readQ()
        return(self.data['status'][remoID])

        
