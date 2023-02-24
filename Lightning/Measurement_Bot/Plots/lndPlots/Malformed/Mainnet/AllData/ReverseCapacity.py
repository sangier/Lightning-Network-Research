import json 
import pandas as pd 

data=pd.read_json("dataPeer1.json")
	
dataFiltered = {}  
dataFiltered['channels'] = []

n=0
for i in data["channels"]:
    if(int(data["channels"][n]["Channel_direction"])==1 and int(data["channels"][n]["EstimatedCapacity"])!=-1 and int(data["channels"][n]["EstimatedCapacity"])!=-2): 
        dataFiltered['channels'].append({  
        'Node1_pub_key': data['channels'][n]['Node1_pub_key'],
        'Node2_pub_key': data['channels'][n]['Node2_pub_key'],
        'Channel_ID': data['channels'][n]['Channel_ID'],
        'Capacity': data['channels'][n]['Capacity'],
        'EstimatedCapacity': int(data['channels'][n]['Capacity'])-int(data['channels'][n]['EstimatedCapacity']),
        'ShortChannelID': data['channels'][n]['ShortChannelID'],
        'Channel_direction': data['channels'][n]['Channel_direction'],
        'MeasurementTime': data['channels'][n]['MeasurementTime'],			
        })
    elif(int(data["channels"][n]["Channel_direction"])==0 and int(data["channels"][n]["EstimatedCapacity"])!=-1 and int(data["channels"][n]["EstimatedCapacity"])!=-2): 
        dataFiltered['channels'].append({  
        'Node1_pub_key': data['channels'][n]['Node1_pub_key'],
        'Node2_pub_key': data['channels'][n]['Node2_pub_key'],
        'Channel_ID': data['channels'][n]['Channel_ID'],
        'Capacity': data['channels'][n]['Capacity'],
        'EstimatedCapacity': int(data['channels'][n]['Capacity'])-int(data['channels'][n]['EstimatedCapacity']),
        'ShortChannelID': data['channels'][n]['ShortChannelID'],
        'Channel_direction': data['channels'][n]['Channel_direction'],
        'MeasurementTime': data['channels'][n]['MeasurementTime'],			
        })
    elif(int(data["channels"][n]["EstimatedCapacity"])==-1 or int(data["channels"][n]["EstimatedCapacity"])==-2): 
        dataFiltered['channels'].append({  
        'Node1_pub_key': data['channels'][n]['Node1_pub_key'],
        'Node2_pub_key': data['channels'][n]['Node2_pub_key'],
        'Channel_ID': data['channels'][n]['Channel_ID'],
        'Capacity': data['channels'][n]['Capacity'],
        'EstimatedCapacity': int(data['channels'][n]['EstimatedCapacity']),
        'ShortChannelID': data['channels'][n]['ShortChannelID'],
        'Channel_direction': data['channels'][n]['Channel_direction'],
        'MeasurementTime': data['channels'][n]['MeasurementTime'],			
        })
    n=n+1
		        		
with open('dataPeer1R.json', 'w') as outfile:  
        json.dump(dataFiltered,outfile,indent=4)