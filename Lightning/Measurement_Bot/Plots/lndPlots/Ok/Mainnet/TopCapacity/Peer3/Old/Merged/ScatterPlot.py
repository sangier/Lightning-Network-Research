import numpy as np
import json
import xlrd
import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd 
from scipy import stats
from scipy.stats import norm
import palettable

#with open('ChannelsLifePeer3.json', encoding="utf8") as f:
#    data = json.loads(f.read())
df = pd.read_json("ChannelsLifePeer3R.json")
print(df)

x=[]
y=[]
k=0

for i in df["channels"]:
    if(int(df["channels"][k]["EstimatedCapacity"])!=-1 and int(df["channels"][k]["EstimatedCapacity"])!=-2): 
        y.append(df["channels"][k]["EstimatedCapacity"])
        x.append(df["channels"][k]["TimeFromMining"])
    k=k+1

# 1000 random integers between 0 and 50


# Positive Correlation with some noise
df = pd.DataFrame({"EstimatedCapacity":y,"TimeFromMining":x})

df.sort_values(by=["TimeFromMining"],inplace=True, ascending=False)
df.reset_index(drop=True,inplace=True)
#np.corrcoef(x, y)
#df = df[df.EstimatedCapacity<3500000]
# plt.scatter(df.TimeFromMining, df.EstimatedCapacity)

# plt.xlabel("TimeFromMining")
# plt.ylabel("EstimatedCapacity")
# plt.suptitle('Correlation')
# plt.margins(0.01)
# plt.show()



ax = df.plot.scatter(x="TimeFromMining", y="EstimatedCapacity")
#df2.plot(ax=ax)
#print(df1)


ax.set_ylabel("Capacity")
ax.set_xlabel("Time From Mining")

fig = ax.get_figure()
fig.savefig('ScatterPeer3.png',bbox_inches='tight')