import json 
import pandas as pd 
import os 

with open('m1graph.json',encoding='utf-8') as f:
    dataNet=json.loads(f.read())


dataFiltered = {}  
dataFiltered['nodes'] = []


j=[]
x=[]
y=[]


k=0



for element in dataNet["nodes"]: 
    j.append(dataNet["nodes"][k]["pub_key"])
    k=k+1
	

dfn=j

k=0
h=0

inc=0
outc=0

for element in dfn: 
    for element2 in dataNet["edges"]:
        if(dfn[k]==dataNet["edges"][h]["node1_pub"]):
            x.append(int(dataNet["edges"][h]["capacity"]))
            outc=outc+1
        elif(dfn[k]==dataNet["edges"][h]["node2_pub"]):
            y.append(int(dataNet["edges"][h]["capacity"]))
            inc=inc+1
        h=h+1
    x1=pd.DataFrame()
    y1=pd.DataFrame()
    x1["OutBoundC"]=x
    y1["InBoundC"]=y
    x1.reset_index(drop=True,inplace=True)
    y1.reset_index(drop=True,inplace=True)
   #print("nodes with pubkey: "+str(dfn[k])+" InBoundC: "+str(y1.InBoundC.sum())+" InChanNumber: "+str(inc)+" OutChanNumber: "+str(outc)+" OutBoundC: "+str(x1.OutBoundC.sum())+" Balance: "+str(y1.InBoundC.sum()-x1.OutBoundC.sum()))
    dataFiltered['nodes'].append({  
        'pub_key': str(dfn[k]),
        'InBoundC': int(y1.InBoundC.sum()),
        'InChanNumber': int(inc),
        'OutBoundC': int(x1.OutBoundC.sum()),
        'OutChanNumber': int(outc),
        'Balance': int(y1.InBoundC.sum()-x1.OutBoundC.sum())
        })
    h=0
    k=k+1
    x=[]
    y=[]
    inc=0
    outc=0



#print(dfn)


		        		
with open('FundingBalance.json', 'w') as outfile:  
        json.dump(dataFiltered,outfile,indent=4)

