import json 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import seaborn as sns 

df = pd.read_json("DataPeer3.json")
print(df)

x=[]
y=[]
z=[]
k=0

for i in df["channels"]:
    if(int(df["channels"][k]["EstimatedCapacity"])!=-1 and int(df["channels"][k]["EstimatedCapacity"])!=-2 and int(df["channels"][k]["Channel_direction"]==0)):
        y.append(df["channels"][k]["EstimatedCapacity"])
        x.append(df["channels"][k]["Capacity"]-df["channels"][k]["EstimatedCapacity"])
        z.append(df["channels"][k]["Capacity"])
    k=k+1

df1=pd.DataFrame()
df1["Capacity"]=z
df1["EstimatedCapacity"]=y
df1["Difference"]=x
df1.sort_values(by=["Capacity"],inplace=True, ascending=False)
df1.reset_index(drop=True,inplace=True)
print(df1)

df2=df1[:50]

df3=pd.DataFrame()
df3["EstimatedCapacity"]=df2["EstimatedCapacity"]
df3["Difference"]=df2["Difference"]

#df2.sort_values(by=["Capacity","EstimatedCapacity"],inplace=True, ascending=False)
#df2.reset_index(drop=True,inplace=True)
print(df3)



#df.diff(axis=1).fillna(df).astype(df.dtypes).plot.bar(stacked=True)


ax=df3.plot.bar(stacked=True)
# #ax=df1[['EstimatedCapacity', 'Capacity']].plot(kind='hist', stacked=True)
ax.set_ylabel("Capacity")
ax.set_xlabel("Channel Number")

fig = ax.get_figure()
fig.savefig('StackedMainPeer3.png',bbox_inches='tight')