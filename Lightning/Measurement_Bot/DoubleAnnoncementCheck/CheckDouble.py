import json 
import pandas as pd 
import os 

with open('mainnet_red_graph.json',encoding='utf-8') as f:
    dataNet=json.loads(f.read())



#with open('dataPeer2.json',encoding='utf-8') as f:
#    data=json.loads(f.read())

dataFiltered = {}  
dataFiltered['channels'] = []

#print(dataNet['edges'][0]['channel_id'])
#print(data['channels'][0]["Channel_ID"])
#print(len(dataNet["edges"]))
#print(len(data["channels"]))


count=0
n=0
p=0
for m in range(0,len(dataNet['edges'])):
    for c in range(0,len(dataNet["edges"])):
        if (dataNet['edges'][n]["channel_id"]==dataNet['edges'][p]['channel_id']):
            count=count+1
        p=p+1
    if(count>1):
        print(count)
        count=0
    else:
        count=0
    n=n+1
    p=0
		        		
#with open('dataFilteredPeer2.json', 'w') as outfile:  
#        json.dump(dataFiltered,outfile,indent=4)
