import json 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import seaborn as sns 

df = pd.read_json("DataPeer1.json")
print(df)

x=[]
y=[]
k=0

for i in df["channels"]:
    if(int(df["channels"][k]["EstimatedCapacity"])!=-1 and int(df["channels"][k]["EstimatedCapacity"])!=-2 and int(df["channels"][k]["Channel_direction"]==0)):
        x.append(df["channels"][k]["EstimatedCapacity"]/df["channels"][k]["Capacity"])
    k=k+1

df1=pd.DataFrame()
#df1["Capacity"]=x
df1["EstimatedCapacity"]=x
df1.sort_values(by=["EstimatedCapacity"],inplace=True, ascending=False)
df1.reset_index(drop=True,inplace=True)
print(df1)

#df2=df1[:50]

print(df1)
ax=df1.plot()

ax.set_ylabel("Capacity")
ax.set_xlabel("Channel Number")
fig = ax.get_figure()
fig.savefig('Norm_PlotMainPeer1.png',bbox_inches='tight')

