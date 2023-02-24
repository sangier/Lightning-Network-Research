from blockchain import blockexplorer
import json 
import pandas as pd 
import os 
import time 

with open('dataFilteredPeer1.json',encoding='utf-8') as f:
    data=json.loads(f.read())

if os.path.exists("ChannelsLifePeer1.json"):
    print("Opening Existing Data File")
    with open('ChannelsLifePeer1.json') as f:
        data1=json.loads(f.read())
else: 
    print("Creating Data File")
    data1 = {}  
    data1['channels'] = []

k=0
j=0
for i in range(0,len(data['channels'])):
    funding=data['channels'][k]["ChannelPoint"]
    funding=funding[:64]
    block=blockexplorer.get_tx(funding).block_height
    print(k)
    block2=blockexplorer.get_block_height(block)
    BlockMiningTime=block2[0].time
    data1['channels'].append({  
    'Node1_pub_key': data['channels'][k]['Node1_pub_key'],
    'Node2_pub_key': data['channels'][k]['Node2_pub_key'],
    'Channel_ID': data['channels'][k]['Channel_ID'],
    'Capacity': data['channels'][k]['Capacity'],
    'EstimatedCapacity': data['channels'][k]['EstimatedCapacity'],
    'ShortChannelID': data['channels'][k]['ShortChannelID'],
    'Channel_direction': data['channels'][k]['Channel_direction'],
    'MeasurementTime': data['channels'][k]['MeasurementTime'],			
    'TimeFundingTxMined': BlockMiningTime,
    'TimeFromMining': (time.time()-BlockMiningTime),
    })
    with open('ChannelsLifePeer1.json', 'w') as outfile:  
        json.dump(data1,outfile,indent=4)
    k=k+1

