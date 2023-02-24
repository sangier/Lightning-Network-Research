import json 
import pandas as pd 
import os 

with open('m1graph.json',encoding='utf-8') as f:
    dataNet=json.loads(f.read())

cc=0
for element in dataNet["edges"]: 
    del element['last_update']

with open('m4graph.json',encoding='utf-8') as f:
    dataNet2=json.loads(f.read())

for element in dataNet2["edges"]: 
    del element['last_update']





#with open('dataPeer2.json',encoding='utf-8') as f:
#    data=json.loads(f.read())

dataFiltered = {}  
dataFiltered['channels'] = []

#print(dataNet['edges'][0]['channel_id'])
#print(data['channels'][0]["Channel_ID"])
#print(len(dataNet["edges"]))
#print(len(data["channels"]))


counterSameChannels=0
counterSameChannelsInfo=0
count=0

internalc=0

n=0
p=0
for m in range(0,len(dataNet['edges'])):
    for c in range(0,len(dataNet2["edges"])):
        if (dataNet['edges'][n]["channel_id"]==dataNet2['edges'][p]['channel_id']):
            count=count+1
            counterSameChannels=counterSameChannels+1
            if(dataNet['edges'][n]==dataNet2['edges'][p]):
                counterSameChannelsInfo=counterSameChannelsInfo+1
            else:
                if(internalc<10):
                    print("Node 1 channel:    ")
                    print(dataNet['edges'][n])
                    print("Node 2 channel:    ")
                    print(dataNet2['edges'][p])
                    internalc=internalc+1
        p=p+1
    if(count>1):
        print(count)
        count=0
    else:
        count=0
    n=n+1
    p=0
	
	
print("Node 1 has: "+str(len(dataNet['edges']))+" channels")
print("Node 2 has: "+str(len(dataNet2['edges']))+" channels")
print("Node1 and Node2 have the same channels_ID for: "+str(counterSameChannels)+" channels")
print("Node1 and Node2 have the same channels info for: "+str(counterSameChannelsInfo)+" channels")