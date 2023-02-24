import networkx as nx 
import matplotlib.pyplot as plt
import json 
import pandas as pd

with open('graph.json', encoding="utf8") as f:
    data=json.loads(f.read())

data1=[]
data2=[]
data3=[]
data4=[]
k=0
for i in data["nodes"]:
    data1.insert(k,data["nodes"][k]["pub_key"])
    k=k+1

#print(data1)


k=0
for i in data["edges"]:
    data2.insert(k,data["edges"][k]["node1_pub"])
    data3.insert(k,data["edges"][k]["node2_pub"])
    data4.insert(k,data["edges"][k]["capacity"])
    k=k+1
	
G=nx.DiGraph()

k=0
for i in data1:
    G.add_node(data1[k])
    k=k+1

k=0

for i in data["edges"]:
    G.add_edge(data2[k],data3[k],weight=int(data4[k]))
    k=k+1

capacities=[]
#TO GET A SPECIFC EDGE CAPACITY
j=0
for j in data["nodes"]:
    k=0
    for i in data["nodes"]:
        capacities.insert(k,G.get_edge_data(data["nodes"][j]["pub_key"], data["nodes"][k]["pub_key"]))
        k=k+1
    j=j+1
	
print(capacities)
#j=0
#for j in data["nodes"]:
#    K=0
#    for i in data["nodes"]:
#        print(G.get_edge_data('02a09f477196886694be593349f5eb76b2f534939d8acca512bef35c418f71025d', all(data["nodes"][K])))
#        K=K+1
		#TO GET ALL THE EDGES
#print(G.edges())


#nx.draw(G, pos=nx.spring_layout(G), nodecolor='r', edge_color='b')
#plt.show()