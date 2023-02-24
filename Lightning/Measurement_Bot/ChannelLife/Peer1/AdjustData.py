import json
import pandas as pd 


with open('ChannelsLifePeer1.json',encoding='utf-8') as f:
    data=json.loads(f.read())
with open('DataPeer1.json',encoding='utf-8') as f:
    data2=json.loads(f.read())
dataFiltered = {}  
dataFiltered['channels'] = []

#print(dataNet['edges'][0]['channel_id'])
#print(data['channels'][0]["Channel_ID"])
#print(len(dataNet["edges"]))
#print(len(data["channels"]))



n=0
p=0
for m in range(0,len(data['channels'])):
    if (data['channels'][n]["Channel_ID"]==data2['channels'][p]['Channel_ID']):
        dataFiltered['channels'].append({  
        'Node1_pub_key': data['channels'][n]['Node1_pub_key'],
        'Node2_pub_key': data['channels'][n]['Node2_pub_key'],
        'Channel_ID': data['channels'][n]['Channel_ID'],
        'Capacity': data['channels'][n]['Capacity'],
        'EstimatedCapacity': data2['channels'][n]['EstimatedCapacity'],
        'ShortChannelID': data2['channels'][n]['ShortChannelID'],
        'Channel_direction': data2['channels'][n]['Channel_direction'],
        'TimeFromMining': data['channels'][n]['TimeFromMining'],			
        'TimeFundingTxMined': data['channels'][p]['TimeFundingTxMined']
        })
    print("Channel_Macth")
    p=p+1
    n=n+1
		        		
with open('ChannelsLifePeer1R.json', 'w') as outfile:  
        json.dump(dataFiltered,outfile,indent=4)
		
		