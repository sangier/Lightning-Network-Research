import json 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import seaborn as sns 

#df = pd.read_json("Mainnet_data.json")
#df = pd.read_json("DataPeer1.json")

df = pd.read_json("dataPeer1.json")
#df=dfap["channels"]

print(df)

#df.sort_values(by=["Capacity"],inplace=True, ascending=False)
#df.reset_index(drop=True,inplace=True)


x=[]
y=[]
k=0

for i in df["channels"]:
    if(int(df["channels"][k]["EstimatedCapacity"])!=-1 and int(df["channels"][k]["EstimatedCapacity"])!=-2): 
        y.append(df["channels"][k]["EstimatedCapacity"])
        x.append(df["channels"][k]["Capacity"])
    k=k+1

df1=pd.DataFrame()
df2=pd.DataFrame()
df1["Capacity"]=x
df2["EstimatedCapacity"]=y
df1.reset_index(drop=True,inplace=True)
df2.reset_index(drop=True,inplace=True)



df1["Capacity"].abs()
df2["EstimatedCapacity"].abs()
print(df1)
print("End of This")
print(df2)

 

print("la somma delle capacità dichiarate è: "+str(df1.sum()))


print("la somma delle capacità misurate è: "+str(df2.sum()))

print("Sono stati spesi: "+str(df1.sum().Capacity -df2.sum().EstimatedCapacity))