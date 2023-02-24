import json 
import pandas as pd 
import os 

with open('FundingBalance.json',encoding='utf-8') as f:
    dataNet=json.loads(f.read())



j=[]
x=[]
y=[]


k=0

posc=0
negc=0
zc=0
for element in dataNet["nodes"]: 
    if(int(dataNet["nodes"][k]["Balance"])>0):
        posc=posc+1
    elif(int(dataNet["nodes"][k]["Balance"])<0):
        negc=negc+1        
    else:
        zc=zc+1
    x.append(dataNet["nodes"][k]["Balance"])
    k=k+1
	
	
df=pd.DataFrame()
df["Balance"]=x


print(df.Balance.sum())

print("There are : "+str(len(dataNet["nodes"]))+" Nodes")
print("Nodes with positive balance are: "+str(posc))
print("Nodes with negative balance are: "+str(negc))
print("Nodes with 0 balance are: "+str(zc))
