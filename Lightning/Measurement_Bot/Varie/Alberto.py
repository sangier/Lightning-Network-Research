import json 
import pandas as pd 

df = pd.read_json("Mainnet_data.json")
df_exceeding =df[df["EstimatedCapacity"] > df["Capacity"]]

print(df_exceeding[["EstimatedCapacity", "Capacity", "Channel_direction"]])

df_max_nonexceeding = df[df["EstimatedCapacity"] < df["Capacity"] +10]
df_max_nonexceeding = df_max_nonexceeding[df_max_nonexceeding["EstimatedCapacity"] > df_max_nonexceeding["Capacity"]]


df_zero = df[df["EstimatedCapacity"]<12]

print(df_zero[["EstimatedCapacity", "Capacity", "Channel_direction"]])

print(len(df))
print(len(df_exceeding))
print(len(df_max_nonexceeding))
print(len(df_zero))

df_middle = df[(df["EstimatedCapacity"]>10) & (df["EstimatedCapacity"]<=df["Capacity"])]
print(df_middle[["EstimatedCapacity", "Capacity", "Channel_direction"]])



        # {
            # "Capacity": 267396, 
            # "MeasurementTime": 12.323125839233398, 
            # "EstimatedCapacity": 10, 
            # "Channel_ID": "603088725007925249", 
            # "Node2_pub_key": "033181a72d4d61c6f3138240d98994e9553726bc65c892e9fe7a7b728a54005a36", 
            # "ShortChannelID": "548506:1572:1", 
            # "Node1_pub_key": "0217890e3aad8d35bc054f43acc00084b25229ecff0ab68debd82883ad65ee8266", 
            # "Channel_direction": 1
        # }, 8382

