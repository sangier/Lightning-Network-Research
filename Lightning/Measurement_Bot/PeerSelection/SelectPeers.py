from blockchain import blockexplorer
import json 
import pandas as pd 
import os 


with open('mainnet_red_graph.json',encoding='utf-8') as f:
    dataNet=json.loads(f.read())

if os.path.exists("NewPeers.json"):
    print("Opening Existing Data File")
    with open('NewPeers.json') as f:
        NewPeers=json.loads(f.read())
else: 
    print("Creating Data File") 
    NewPeers= []


with open('dataPeer1.json',encoding='utf-8') as f:
    data=json.loads(f.read())





n=0
p=0
for m in range(0,len(data['channels'])):
    for c in range(0,len(dataNet["nodes"])):
        if (data['channels'][n]["Node1_pub_key"]=="0217890e3aad8d35bc054f43acc00084b25229ecff0ab68debd82883ad65ee8266" and data['channels'][n]["Channel_direction"]==0 and data['channels'][n]["EstimatedCapacity"]>=data['channels'][n]["Capacity"]):
            if (data['channels'][n]["Node2_pub_key"]==dataNet['nodes'][p]['pub_key']):
                if(dataNet['nodes'][p]['addresses']!=[]):
                    NewPeers.append({  
                    'Address': dataNet['nodes'][p]['pub_key'],
                    'Address_IP': str(dataNet['nodes'][p]['pub_key'])+"@"+str(dataNet['nodes'][p]['addresses'][0]["addr"]),
                    })
            
        p=p+1
    n=n+1
    p=0
		        		
with open('NewPeers.json', 'w') as outfile:  
        json.dump(NewPeers,outfile,indent=4)

		


with open('dataPeer2.json',encoding='utf-8') as f:
    data=json.loads(f.read())

n=0
p=0
for m in range(0,len(data['channels'])):
    for c in range(0,len(dataNet["nodes"])):
        if (data['channels'][n]["Node1_pub_key"]=="03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f" and data['channels'][n]["Channel_direction"]==0 and data['channels'][n]["EstimatedCapacity"]>=data['channels'][n]["Capacity"]):
            if (data['channels'][n]["Node2_pub_key"]==dataNet['nodes'][p]['pub_key']):
                if(dataNet['nodes'][p]['addresses']!=[]):
                    NewPeers.append({  
                    'Address': dataNet['nodes'][p]['pub_key'],
                    'Address_IP': str(dataNet['nodes'][p]['pub_key'])+"@"+str(dataNet['nodes'][p]['addresses'][0]["addr"]),
                    })
            
        p=p+1
    n=n+1
    p=0
		        		
with open('NewPeers.json', 'w') as outfile:  
        json.dump(NewPeers,outfile,indent=4)

		
		
		
with open('dataPeer3.json',encoding='utf-8') as f:
    data=json.loads(f.read())

n=0
p=0
for m in range(0,len(data['channels'])):
    for c in range(0,len(dataNet["nodes"])):
        if (data['channels'][n]["Node1_pub_key"]=="0279c22ed7a068d10dc1a38ae66d2d6461e269226c60258c021b1ddcdfe4b00bc4" and data['channels'][n]["Channel_direction"]==0 and data['channels'][n]["EstimatedCapacity"]>=data['channels'][n]["Capacity"]):
            if (data['channels'][n]["Node2_pub_key"]==dataNet['nodes'][p]['pub_key']):
                if(dataNet['nodes'][p]['addresses']!=[]):
                    NewPeers.append({  
                    'Address': dataNet['nodes'][p]['pub_key'],
                    'Address_IP': str(dataNet['nodes'][p]['pub_key'])+"@"+str(dataNet['nodes'][p]['addresses'][0]["addr"]),
                    })
            
        p=p+1
    n=n+1
    p=0
		        		
with open('NewPeers.json', 'w') as outfile:  
        json.dump(NewPeers,outfile,indent=4)
