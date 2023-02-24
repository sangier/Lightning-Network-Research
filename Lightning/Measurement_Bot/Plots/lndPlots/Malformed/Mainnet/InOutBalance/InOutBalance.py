import json 
import pandas as pd 

data=pd.read_json("Peer1_2_3.json")

dataDif=pd.read_json("Connected_Peers.json")



dataFiltered = {}  
dataFiltered['channels'] = []

j=0
n=0
for i in data["channels"]:
    if(int(data["channels"][n]["EstimatedCapacity"])!=-1 and int(data["channels"][n]["EstimatedCapacity"])!=-2): 
        for q in dataDif["channels"]:
            if(data["channels"][n]["Channel_ID"]==dataDif["channels"][j]["Channel_ID"]):
                if(data["channels"][n]["Channel_direction"]!=dataDif["channels"][j]["Channel_direction"]):
                    print("Canali con direzioni diverse: ok")
                    if(int(data["channels"][n]["Channel_direction"])==0):
                        dataFiltered['channels'].append({  
                       'Node1_pub_key': data['channels'][n]['Node1_pub_key'],
                       'Node2_pub_key': data['channels'][n]['Node2_pub_key'],
                       'Channel_ID': data['channels'][n]['Channel_ID'],
                       'Capacity': data['channels'][n]['Capacity'],
                       'EstimatedCapacityNode1': int(data['channels'][n]['EstimatedCapacity']),
                       'GastadosNode1': data['channels'][n]['Capacity']-int(data['channels'][n]['EstimatedCapacity']),
                       'EstimatedCapacityNode2': int(dataDif['channels'][j]['EstimatedCapacity']),
                       #'GastadosNode2': int(dataDif['channels'][j]['Capacity'])-int(dataDif['channels'][j]['EstimatedCapacity']),
                       'ShortChannelID': data['channels'][n]['ShortChannelID'],
                       'Channel_directionPeer1': data['channels'][n]['Channel_direction'],
                       'Channel_directionPeer2': dataDif['channels'][j]['Channel_direction'],
                       'Balance': (int(data['channels'][n]['Capacity'])-int(data['channels'][n]['EstimatedCapacity'])) -int(dataDif['channels'][j]['EstimatedCapacity']),
                       })
                    else:
                        dataFiltered['channels'].append({  
                       'Node1_pub_key': data['channels'][n]['Node1_pub_key'],
                       'Node2_pub_key': data['channels'][n]['Node2_pub_key'],
                       'Channel_ID': data['channels'][n]['Channel_ID'],
                       'Capacity': data['channels'][n]['Capacity'],
                       'EstimatedCapacityNode1': int(data['channels'][n]['EstimatedCapacity']),
                       #'GastadosNode1': data['channels'][n]['Capacity']-int(data['channels'][n]['EstimatedCapacity']),
                       'EstimatedCapacityNode2': int(dataDif['channels'][j]['EstimatedCapacity']),
                       'GastadosNode2': int(dataDif['channels'][j]['Capacity'])-int(dataDif['channels'][j]['EstimatedCapacity']),
                       'ShortChannelID': data['channels'][n]['ShortChannelID'],
                       'Channel_directionPeer1': data['channels'][n]['Channel_direction'],
                       'Channel_directionPeer2': dataDif['channels'][j]['Channel_direction'],
                       'Balance': (int(dataDif['channels'][j]['Capacity'])-int(dataDif['channels'][j]['EstimatedCapacity'])) -int(data['channels'][n]['EstimatedCapacity']),
                       })
                else:
                    print("I canali hanno la stessa direzione... mmmmm")
            j=j+1
    n=n+1
    j=0
		        		
with open('Comparison.json', 'w') as outfile:  
        json.dump(dataFiltered,outfile,indent=4)