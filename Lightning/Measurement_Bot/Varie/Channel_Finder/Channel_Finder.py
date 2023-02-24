import networkx as nx 
import matplotlib.pyplot as plt
import json 
import pandas as pd

with open('testnet_graph.json', encoding="utf8") as f:
    data=json.loads(f.read())

data1=[]
data2=[]
data3=[]
data4=[]
data5=[]

k=0
for i in data["nodes"]:
    data1.insert(k,data["nodes"][k]["pub_key"])
    k=k+1

#print(data1)
#Node under test 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 0270685ca81a8e4d4d01beec5781f4cc924684072ae52c507f8ebe9daf0caaab7b 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 1600706411112235008 100000

#0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f

#Our chanel is open with 0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f

#Node 03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975

k=0
for i in data["edges"]:
    if data["edges"][k]["node1_pub"]=="0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f":
        if data["edges"][k]["node1_policy"]["disabled"]== 0:
            if data["edges"][k]["node2_policy"]["disabled"]== 0:
                data2.insert(k,data["edges"][k]["node1_pub"])
                data3.insert(k,data["edges"][k]["node2_pub"])
                data4.insert(k,data["edges"][k]["capacity"])
                data5.insert(k,data["edges"][k]["channel_id"])
    k=k+1

dataJson={}

dataJson['channels'] = []
k=0
for i in data2:
    dataJson['channels'].append({  
            'node1_pub': data2[k],
            'node2_pub': data3[k],
            'channel_id': data5[k],
			'capacity': data4[k],
			'real_capacity':0,
            })
    k=k+1

with open('data_test.json', 'w') as outfile:  
    json.dump(dataJson,outfile,indent=4)
	

with open('data_test.json', encoding="utf8") as f:
    dataPrint=json.loads(f.read())
	
print(dataPrint)