import json 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import seaborn as sns 

#df = pd.read_json("Mainnet_data.json")
df = pd.read_json("MixedMainnetDataMod.json")
print(df)


df.sort_values(by=["Capacity"],inplace=True, ascending=False)
df.reset_index(drop=True,inplace=True)


df1=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
print(df)

#if(["EstimatedCapacity"]!=-1 and ["EstimatedCapacity"]!=-2 and ["Channel_direction"]==0): 

df1=df[df.EstimatedCapacity!=-1]
df3=df1[df1.EstimatedCapacity!=-2] 
#df3=df2[df2.Channel_direction!=0]
df3.reset_index(drop=True,inplace=True)
print("allora 3")
print(df3)
#df1["Capacity"]=x
#df2["EstimatedCapacity"]=y
#df1.sort_values(by=["Capacity"],inplace=True, ascending=False)
#df1.reset_index(drop=True,inplace=True)
#df2.sort_values(by=["EstimatedCapacity"],inplace=True, ascending=False)
#df2.reset_index(drop=True,inplace=True)

#df1["Capacity"].abs()
df3["EstimatedCapacity"].abs()
#print(df1)
print("End of This")
#print(df2)

ax=df3.plot(y=['Capacity', 'EstimatedCapacity'], figsize=(10,5), grid=True)

#df2=df1[:50]
#ax = df.plot(4)
#df.plot(5,ax=ax)
#print(df1)


ax.set_ylabel("Capacity")
ax.set_xlabel("Channel")
ax.set_title("InOut Channels Peers 1 2 3")

fig = ax.get_figure()
fig.savefig('InOutMixedtPeers123_1.png',bbox_inches='tight')


 #pscp sangieri@163.117.166.221:Boot_Testnet.py sangieri@192.168.122.12:Boot_Testnet.py