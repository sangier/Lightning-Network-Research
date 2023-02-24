import json 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import seaborn as sns 

#df = pd.read_json("Mainnet_data.json")
df = pd.read_json("AllMixedMainnetData.json")
print(df)

x=[]
y=[]
k=0

for i in df["channels"]:
    if(int(df["channels"][k]["EstimatedCapacity"])!=-1 and int(df["channels"][k]["EstimatedCapacity"])!=-2 and int(df["channels"][k]["Channel_direction"]==1)): 
        y.append(df["channels"][k]["EstimatedCapacity"])
        x.append(df["channels"][k]["Capacity"])
    k=k+1

df1=pd.DataFrame()
df2=pd.DataFrame()
df1["Capacity"]=x
df2["EstimatedCapacity"]=y
df1.sort_values(by=["Capacity"],inplace=True, ascending=False)
df1.reset_index(drop=True,inplace=True)
df2.sort_values(by=["EstimatedCapacity"],inplace=True, ascending=False)
df2.reset_index(drop=True,inplace=True)

df1["Capacity"].abs()
df2["EstimatedCapacity"].abs()
print(df1)
print("End of This")
print(df2)

#df2=df1[:50]
ax = df1.plot()
df2.plot(ax=ax)
#print(df1)


ax.set_ylabel("Capacity")
ax.set_xlabel("Channel")
ax.set_title("In Channels Mixed")

fig = ax.get_figure()
fig.savefig('InMixed.png',bbox_inches='tight')


 #pscp sangieri@163.117.166.221:Boot_Testnet.py sangieri@192.168.122.12:Boot_Testnet.py