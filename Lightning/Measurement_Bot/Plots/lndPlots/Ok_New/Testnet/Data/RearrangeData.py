from blockchain import blockexplorer
import json 
import pandas as pd 
import os 
import time 

with open('Testnet_data.json',encoding='utf-8') as f:
    data=json.loads(f.read())
	
print("Creating Data File")
data1 = {}  
data1['channels'] = []

k=0
j=0
for i in range(0,len(data['channels'])):
    if(int(data['channels'][k]['EstimatedCapacity'])==10 and  int(data['channels'][k]['Channel_direction'])==0):
        data1['channels'].append({  
        'Node1_pub_key': data['channels'][k]['Node1_pub_key'],
        'Node2_pub_key': data['channels'][k]['Node2_pub_key'],
        'Channel_ID': data['channels'][k]['Channel_ID'],
        'Capacity': data['channels'][k]['Capacity'],
        'EstimatedCapacity': data['channels'][k]['Capacity'],
        'ShortChannelID': data['channels'][k]['ShortChannelID'],
        'Channel_direction': data['channels'][k]['Channel_direction'],
        'MeasurementTime': data['channels'][k]['MeasurementTime'],			
        })
        with open('Testnet_data_2.json', 'w') as outfile:
             json.dump(data1,outfile,indent=4)
    else:
        data1['channels'].append({  
        'Node1_pub_key': data['channels'][k]['Node1_pub_key'],
        'Node2_pub_key': data['channels'][k]['Node2_pub_key'],
        'Channel_ID': data['channels'][k]['Channel_ID'],
        'Capacity': data['channels'][k]['Capacity'],
        'EstimatedCapacity': data['channels'][k]['EstimatedCapacity'],
        'ShortChannelID': data['channels'][k]['ShortChannelID'],
        'Channel_direction': data['channels'][k]['Channel_direction'],
        'MeasurementTime': data['channels'][k]['MeasurementTime'],			
        })
        with open('Testnet_data_2.json', 'w') as outfile:
            json.dump(data1,outfile,indent=4)
    k=k+1
	    

