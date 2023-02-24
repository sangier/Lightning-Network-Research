import json

data1=[]
data = {}  
data['edges'] = []  
data['edges'].append({  
    'Node1_pub_key': 'Scott',
    'Node2_pub_key': 'stackabuse.com',
    'Channel_ID': 'Nebraska',
    'Short_Channel_ID': 'test',
    'Capacity': 'test22',
    'Real_Capacity': 'test222', 	
})

data['edges'].append({  
    'Node1_pub_key': 'un nuodo a casa',
    'Node2_pub_key': 'stackabuse.aaaaaa',
    'Channel_ID': 'Nebraskssssa',
    'Short_Channel_ID': 'test22111212',
    'Capacity': 'test2121212',
    'Real_Capacity': 'test21212122', 	
})
data['edges'].append({  
    'Node1_pub_key': 'Scottishhhh',
    'Node2_pub_key': 'stackabuse.asasacom',
    'Channel_ID': 'Nebraskfffffa',
    'Short_Channel_ID': 'test11111111',
    'Capacity': 'test2331212',
    'Real_Capacity': 'test22121212', 	
})

with open('data.json', 'w') as outfile:  
    json.dump(data,outfile,indent=4)
	

with open('data.json', encoding="utf8") as f:
    data1=json.loads(f.read())

print(data1)