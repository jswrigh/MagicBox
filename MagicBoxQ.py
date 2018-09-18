import json

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

    def writeQ(self):
        print(self.data)
        with open('data.txt', 'w') as outfile:  
            json.dump(self.data, outfile)

    def readQ(self):
        with open('data.txt') as json_file:  
            data = json.load(json_file)
            print(data)
            print('Inside Temperature: ' + data['environment']['insideTemp'])
            print('Outside Temperature: ' + data['environment']['outsideTemp'])
            print('insideHumidity: ' + data['environment']['insideHumidity'])
            print('')
            print('Set Temperature: ' +data['settings']['setTemp'])
            print('Desired Adjustment: ' +data['settings']['iFeel'])
        
