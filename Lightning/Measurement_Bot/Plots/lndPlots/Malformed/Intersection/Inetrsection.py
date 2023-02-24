from blockchain import blockexplorer
import json 
import pandas as pd 
import os 



#with open('dataPeer2.json',encoding='utf-8') as f:
#    data=json.loads(f.read())
data = pd.read_json("dataPeer2.json")


print(type(data))

#intersection_df = data[data['Node1_pub_key'] == "0217890e3aad8d35bc054f43acc00084b25229ecff0ab68debd82883ad65ee8266" & data['Node2_pub_key'] == "03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f"]
#intersection_df2 = data[data['Node1_pub_key'] == "03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f" & data['Node2_pub_key'] == "0217890e3aad8d35bc054f43acc00084b25229ecff0ab68debd82883ad65ee8266"]
	
intersection_df = data[data['Node1_pub_key'] == "0217890e3aad8d35bc054f43acc00084b25229ecff0ab68debd82883ad65ee8266"]
intersection_df2 = data[data['Node2_pub_key'] == "0217890e3aad8d35bc054f43acc00084b25229ecff0ab68debd82883ad65ee8266"]

#intersection_df = data[ data['Node1_pub_key'] == "03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f"]

	
print(intersection_df)
print(intersection_df2)


	



