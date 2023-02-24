from blockchain import blockexplorer
import json 
import pandas as pd 
import os 


with open('mainnet_red_graph.json',encoding='utf-8') as f:
    dataNet=json.loads(f.read())



with open('dataPeer3.json',encoding='utf-8') as f:
    data=json.loads(f.read())

dataFiltered = {}  
dataFiltered['channels'] = []

#print(dataNet['edges'][0]['channel_id'])
#print(data['channels'][0]["Channel_ID"])
#print(len(dataNet["edges"]))
#print(len(data["channels"]))



n=0
p=0
for m in range(0,len(data['channels'])):
    for c in range(0,len(dataNet["edges"])):
        if (data['channels'][n]["Channel_ID"]==dataNet['edges'][p]['channel_id']):
            dataFiltered['channels'].append({  
            'Node1_pub_key': data['channels'][n]['Node1_pub_key'],
            'Node2_pub_key': data['channels'][n]['Node2_pub_key'],
            'Channel_ID': data['channels'][n]['Channel_ID'],
            'Capacity': data['channels'][n]['Capacity'],
            'EstimatedCapacity': data['channels'][n]['EstimatedCapacity'],
            'ShortChannelID': data['channels'][n]['EstimatedCapacity'],
            'Channel_direction': data['channels'][n]['EstimatedCapacity'],
            'MeasurementTime': data['channels'][n]['EstimatedCapacity'],			
            'ChannelPoint': dataNet['edges'][p]['chan_point']
            })
            print("Channel_Macth")
        p=p+1
    n=n+1
    p=0
		        		
with open('dataFilteredPeer3.json', 'w') as outfile:  
        json.dump(dataFiltered,outfile,indent=4)
