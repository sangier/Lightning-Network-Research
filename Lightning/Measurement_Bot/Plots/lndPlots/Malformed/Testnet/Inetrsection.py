from blockchain import blockexplorer
import json 
import pandas as pd 
import os 



#with open('dataPeer2.json',encoding='utf-8') as f:
#    data=json.loads(f.read())
data = pd.read_json("Testnet_data4.json")


print(type(data))


#intersection_df = data[data['Node1_pub_key'] == "02a68237add204623021d09b0334c4992c132eb3c9dcfcb8f3cf8a57386775538e"]
#intersection_df2 = data[data['Node2_pub_key'] == "02a68237add204623021d09b0334c4992c132eb3c9dcfcb8f3cf8a57386775538e"]
	
#intersection_df = data[data['Node1_pub_key'] == "038863cf8ab91046230f561cd5b386cbff8309fa02e3f0c3ed161a3aeb64a643b9"]
#intersection_df2 = data[data['Node2_pub_key'] == "038863cf8ab91046230f561cd5b386cbff8309fa02e3f0c3ed161a3aeb64a643b9"]

#intersection_df = data[data['Node1_pub_key'] == "03236a685d30096b26692dce0cf0fa7c8528bdf61dbf5363a3ef6d5c92733a3016"]
#intersection_df2 = data[data['Node2_pub_key'] == "03236a685d30096b26692dce0cf0fa7c8528bdf61dbf5363a3ef6d5c92733a3016"]

#intersection_df = data[data['Node1_pub_key'] == "02312627fdf07fbdd7e5ddb136611bdde9b00d26821d14d94891395452f67af248"]
#intersection_df2 = data[data['Node2_pub_key'] == "02312627fdf07fbdd7e5ddb136611bdde9b00d26821d14d94891395452f67af248"]    #17    357388  1597682754138537984                  0      ...        0260d9119979caedc570ada883ff614c6efb93f7f7382e...  02312627fdf07fbdd7e5ddb136611bdde9b00d26821d14

intersection_df = data[data['Node1_pub_key'] == "0260d9119979caedc570ada883ff614c6efb93f7f7382e25d73ecbeba0b62df2d7"]
intersection_df2 = data[data['Node2_pub_key'] == "0260d9119979caedc570ada883ff614c6efb93f7f7382e25d73ecbeba0b62df2d7"]    #SI SHORT CHAN ID 1412640:3298:1 INTERSECTION peer 4 e 5




#intersection_df = data[ data['Node1_pub_key'] == "03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f"]

	
print(intersection_df)
print(intersection_df2)


	



