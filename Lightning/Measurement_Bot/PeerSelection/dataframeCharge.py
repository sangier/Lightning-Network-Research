import pandas as pd 
import json 


df= pd.read_json("NewPeersFiltered.json")
df.reset_index(drop=True,inplace=True)

peerList=[]
peerList_ip=[]
peerList.append(df["Address"])
peerList_ip.append(df["Address_IP"])

print(len(peerList_ip[0]))

print("SOTAMAYOR")

#print(peerList_ip)

