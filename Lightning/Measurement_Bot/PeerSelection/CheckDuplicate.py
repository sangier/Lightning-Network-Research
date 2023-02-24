import json 
import pandas as pd 
import os 

with open('NewPeers.json') as f:
        dataNet=json.loads(f.read())


print(dataNet[0]['Address'],len(dataNet))

count=0
n=0
p=0
for m in range(0,len(dataNet)):
    for c in range(0,len(dataNet)):
        if (dataNet[n]['Address']==dataNet[p]['Address']):
            count=count+1
        p=p+1
    if(count>1):
        print(count)
        count=0
    else:
        count=0
    n=n+1
    p=0



