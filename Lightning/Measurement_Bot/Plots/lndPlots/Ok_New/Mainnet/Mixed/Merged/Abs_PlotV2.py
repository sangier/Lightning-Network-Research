import json 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import seaborn as sns 

#df = pd.read_json("Mainnet_data.json")
df = pd.read_json("AllMixedMainnetDataMod.json")
print(df)


df.sort_values(by=["Capacity"],inplace=True, ascending=False)
df.reset_index(drop=True,inplace=True)


df1=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
df4=pd.DataFrame()
df5=pd.DataFrame()

print(df)

#if(["EstimatedCapacity"]!=-1 and ["EstimatedCapacity"]!=-2 and ["Channel_direction"]==0): 


convert_dict = {'Capacity': float, 
                'EstimatedCapacity': float
               } 
  

df = df.astype(convert_dict) 
print(df.dtypes) 

df1=df[df.EstimatedCapacity!=-1]
df3=df1[df1.EstimatedCapacity!=-2] 
#df3=df2[df2.Channel_direction!=1]
df3.reset_index(drop=True,inplace=True)





df4=df3.Capacity/df3.Capacity[0] 
df5=df3.EstimatedCapacity/df3.Capacity[0]

print(df4)


print("allora 3")
print("End of This")
print(df5)
#ax=df3.plot(y=['Capacity', 'EstimatedCapacity'], figsize=(10,5), grid=True)


ax = df4.plot(figsize=(10,5), grid=True)
df5.plot(ax=ax)


ax.set_ylabel("Capacity")
ax.set_xlabel("Channel")
ax.set_title("In Channels Peers 1 ")

fig = ax.get_figure()
fig.savefig('InPeer1_1.png',bbox_inches='tight')



ax.set_ylabel("Capacity")
ax.set_xlabel("Channel")
ax.set_title("InOut Channels Mixed")

fig = ax.get_figure()
fig.savefig('InOutMixedt1.png',bbox_inches='tight')


 #pscp sangieri@163.117.166.221:Boot_Testnet.py sangieri@192.168.122.12:Boot_Testnet.py