import networkx as nx 
import matplotlib.pyplot as plt
import json 
import pandas as pd

with open('mainnet_graph.json', encoding="utf8") as f:
    data=json.loads(f.read())

data1=[]
data2=[]
data3=[]
data4=[]
data5=[]

data 
#k=0
#for i in data["nodes"]:
#    data1.insert(k,data["nodes"][k]["pub_key"])
#    k=k+1

#print(data1)
#Node under test 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 0270685ca81a8e4d4d01beec5781f4cc924684072ae52c507f8ebe9daf0caaab7b 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 1600706411112235008 100000

#k=0
#for i in data["edges"]:
#    if data["edges"][k]["node1_pub"]=="0270685ca81a8e4d4d01beec5781f4cc924684072ae52c507f8ebe9daf0caaab7b":
#        if data["edges"][k]["node1_policy"]["disabled"]== 0:
#            data2.insert(k,data["edges"][k]["node1_pub"])
#            data3.insert(k,data["edges"][k]["node2_pub"])
#            data4.insert(k,data["edges"][k]["capacity"])
#            data5.insert(k,data["edges"][k]["channel_id"])
#    k=k+1
	


k=0 
for i in data["edges"]:
    if int(data["edges"][k]["capacity"])>4294000:
        data2.insert(k,data["edges"][k]["capacity"])
    else:
        data3.insert(k,data["edges"][k]["capacity"])
    k=k+1

print(len(data2),len(data3))
print(len(data2)+(len(data3)))
xper=(len(data2)+len(data3))/100


x1=len(data2)/xper
x2=len(data3)/xper

x11="minor:"
x22="  mayor:"
print(x11,x1,x22,x2)

#G=nx.DiGraph()

#k=0
#for i in data1:
#    G.add_node(data1[k])
#    k=k+1

#k=0

#for i in data["edges"]:
#    G.add_edge(data2[k],data3[k],weight=int(data4[k]))
#    k=k+1
#k=0
#for i in data2:
#    print(data2[k],data3[k],data5[k],data4[k])
#    k=k+1

#print(G.get_edge_data('02a09f477196886694be593349f5eb76b2f534939d8acca512bef35c418f71025d', all(data["nodes"][K])))

#print(G.edges())


#nx.draw(G, pos=nx.spring_layout(G), nodecolor='r', edge_color='b')
#plt.show()