import json 
import pandas as pd 
import os 

import pandas as pd 
  
# making data frame from csv file 
data = pd.read_json("NewPeers.json") 
 
print(len(data))  
# dropping ALL duplicte values 
data.drop_duplicates(subset ="Address", keep = False, inplace = True) 

data.to_json("NewPeersFiltered.json")

data2=pd.read_json("NewPeersFiltered.json")

print(len(data2))

print(data2)