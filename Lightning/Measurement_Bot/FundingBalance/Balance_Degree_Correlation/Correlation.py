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

with open('FundingBalance.json', encoding="utf8") as f:
    data = json.loads(f.read())
data1=[]
data2=[]
data1Nor=[]


k=0
for i in data["nodes"]:    
    data1.insert(k,((int(data["nodes"][k]["Balance"])/100000000)*7014.15))
    k=k+1
	
#print(data["edges"][1]["node1_policy"]["min_htlc"])


#print (sum(data1))

#data1Nor=[data1/sum(data1)]

h=0
for j in data["nodes"]:
    data2.insert(h,(int(data["nodes"][h]["InChanNumber"]))+(int(data["nodes"][h]["OutChanNumber"])))
    h=h+1
		

# 1000 random integers between 0 and 50
x = data2


# Positive Correlation with some noise
y = data1
df = pd.DataFrame({"Degree":y,"Balance":x})

#np.corrcoef(x, y)
#df = df[df.Fee<5000]
plt.scatter(df.Balance, df.Degree)

plt.xlabel("Degree")
plt.ylabel("Balance In Euro")
plt.suptitle('Correlation')
plt.margins(0.02)

plt.show()

	
#plot.show()