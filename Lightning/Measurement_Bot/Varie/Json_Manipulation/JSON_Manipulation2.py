import json
import os 


if os.path.exists("data.json"):
    print("esiste fra")
    with open('data.json',encoding="utf8") as f:
        data=json.loads(f.read())
else: 
    print("non esiste fra")
    data = {}  
    data['channels'] = []


  
data['channels'].append({  
    'Node1_pub_key': 'Scott',
    'Node2_pub_key': 'stackabuse.com',
    'Channel_ID': 'Nebraska',
    'Short_Channel_ID': 'test',
    'Capacity': 'test22',
    'Real_Capacity': 'test222', 	
})


#iter(data).next()['edges'] = var


with open('data.json', 'w') as outfile:  
    json.dump(data,outfile,indent=4)
	

with open('data.json', encoding="utf8") as f:
    dataPrint=json.loads(f.read())
	
print(dataPrint)