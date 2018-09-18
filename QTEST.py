import json

data = {}  
#data['people'] = []  
data['people'] = {  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
}

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)

with open('data.txt') as json_file:  
    data = json.load(json_file)
    print('Name: ' + data['people']['name'])
    print('Website: ' + data['people']['website'])
    print('From: ' + data['people']['from'])
    print('')
