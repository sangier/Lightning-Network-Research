import json 
import subprocess
import time 
import os 
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome
#Step 1: Connection to target peer

address="0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f@197.155.6.38:9735"
cmd="lncli -network=testnet connect "+address
with open('Connection_Log.txt', 'w+') as log:
    c = subprocess.Popen([cmd], stdout=log, stderr=log, shell=True)
    time.sleep(0.5)

res=-1
with open('Connection_Log.txt', 'r+') as f:
    now=f.read()
    if now.startswith("[lncli] rpc error: code = Unknown desc = already connected to peer: "):
        res=0
        print("Peer Arleady Connected")
    if res==-1:
        if now.startswith("[lncli]"): 
            print("Connection Error:")
            print(res)
            print(now)
        elif now.startswith("{"):
            res=1
            print("Connection Established")
            print(res)
            print(now) 

#Step 2: Channel Creation 

value=1000000
address_only_pub="0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f"
cmd2="lncli -network=testnet openchannel "+address_only_pub+" "+str(value)

if res==1 or res==0:
    with open('Channel_Establishment_Log.txt', 'w+') as log2:
        c = subprocess.Popen([cmd2], stdout=log2, stderr=log2, shell=True)
        time.sleep(10)

    res2=0		
    with open('Channel_Establishment_Log.txt', 'r+') as f2:
        now2=f2.read()
        if now2.startswith("[lncli]"):
            res2=-1
            print("Channel Establishment failed:")
            print(res2)
            print(now2)
        elif now2.startswith("{"):
            res2=1
            print("Channel Created!")
            print(res2)
            print(now2) 
else:
    print("There was a Connection Error")
	 

#Step 3: Retrieve all channel owned by the target peer 

with open('Pointer.txt', 'r+') as pointer:
    p=pointer.read()

p=int(p)


if p==0:
    with open('testnet_graph.json') as f:
        data=json.loads(f.read())
    dataJson={}
    dataJson['channels'] = []
    k=0
    for i in data["edges"]:
        if data["edges"][k]["node1_pub"]==address_only_pub:
            if data["edges"][k]["node1_policy"]["disabled"]== 0:
                if data["edges"][k]["node2_policy"]["disabled"]== 0:
                    dataJson['channels'].append({  
                'node1_pub': data["edges"][k]["node1_pub"],
                'node2_pub': data["edges"][k]["node2_pub"],
                'channel_id': data["edges"][k]["channel_id"],
			    'capacity': data["edges"][k]["capacity"],
			    'real_capacity':-1,
                })
        k=k+1
    with open('data_test.json', 'w') as outfile:  
        json.dump(dataJson,outfile,indent=4)
	

with open('data_test.json') as f:
    Channel_Data=json.loads(f.read())
	

#Step 4: Choose one of the available channels 


choosed_peer=""
capacity_cp=0

num_chan=(len(Channel_Data['channels']))

if p==num_chan:
    print("All channel have been tested")  #shall we put this in a variable and analize this variable before proceding to query route steps.
else:
    for i in range(0,num_chan):
        print(i)
        if 	Channel_Data["channels"][p]["real_capacity"]==-1:
            if int(Channel_Data["channels"][p]["capacity"])>=4294967:	
                print("something")
                Channel_Data["channels"][p]["real_capacity"]=-2
            else:
                capacity_cp= Channel_Data["channels"][p]["capacity"]
                choosed_peer=Channel_Data["channels"][p]["node2_pub"]
                p=p+1
                break
        p=p+1
    with open('Pointer.txt', 'w+') as pointer:
        pointer.write(str(p))
    with open('data_test.json', 'w') as outfile:  
        json.dump(Channel_Data,outfile,indent=4)
    with open('data_test.json') as f:
        Channel_Data=json.loads(f.read())	
print(p)
print (capacity_cp)
print(choosed_peer)


#Step 5: Query Routes + Select Route 
lncli -network=testnet queryroutes 03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975 900000 --final_cltv_delta=144

cmd3="lncli -network=testnet queryroutes "+choosed_peer+" "+capacity_cp+" --final_cltv_delta=144"
with open('MyRoute.json', 'w+') as log3:
    c = subprocess.Popen([cmd3], stdout=log3, stderr=log3, shell=True)
    time.sleep(10)

with open('MyRoute.json') as f:
    data=json.loads(f.read())

dataJson={}

dataJson['routes'] = []
dataPrint=[]


#address_only_pub="0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f"
#choosed_peer="03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975"
#first hop : 0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f Previous: 038863cf8ab91046230f561cd5b386cbff8309fa02e3f0c3ed161a3aeb64a643b9
#second hoP: 03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975  Previous: 02fd753c8ad77d2601637b6add4362fec59f4d3e8190347ab4d155f3e9a76e113c
	
k=0 

for i in data:
    if data["routes"][k]["hops"][0]["pub_key"]==address_only_pub or data["routes"][k]["hops"][0]["pub_key"]==choosed_peer:
        if data["routes"][k]["hops"][1]["pub_key"]==address_only_pub or data["routes"][k]["hops"][1]["pub_key"]==choosed_peer:
            dataJson['routes'].append({  
            'total_time_lock': data['routes'][k]['total_time_lock'],
            'total_fees': data['routes'][k]['total_fees'],
            'total_amt': data['routes'][k]['total_amt'],
            })
            dataJson['routes'][0]['hops']=[]
            dataJson['routes'][0]['hops'].append({
	        "chan_id": data["routes"][k]["hops"][0]['chan_id'],
            "chan_capacity": data["routes"][k]["hops"][0]['chan_capacity'],
            "amt_to_forward": data["routes"][k]["hops"][0]['amt_to_forward'],
            "fee": data["routes"][k]["hops"][0]['fee'],
            "expiry": data["routes"][k]["hops"][0]['expiry'],
            "amt_to_forward_msat": data["routes"][k]["hops"][0]['amt_to_forward_msat'],
            "fee_msat": data["routes"][k]["hops"][0]['fee_msat'],
            "pub_key": data["routes"][k]["hops"][0]['pub_key'] 	
            })
            dataJson['routes'][0]['hops'].append({
	        "chan_id": data["routes"][k]["hops"][1]['chan_id'],
            "chan_capacity": data["routes"][k]["hops"][1]['chan_capacity'],
            "amt_to_forward": data["routes"][k]["hops"][1]['amt_to_forward'],
            "fee": data["routes"][k]["hops"][1]['fee'],
            "expiry": data["routes"][k]["hops"][1]['expiry'],
            "amt_to_forward_msat": data["routes"][k]["hops"][1]['amt_to_forward_msat'],
            "fee_msat": data["routes"][k]["hops"][1]['fee_msat'],
            "pub_key": data["routes"][k]["hops"][1]['pub_key'] 	
            })
            dataJson['routes'][0]['hops'].append({
            "chan_id": "1602118184053178368",
            "chan_capacity": "500000",
            "amt_to_forward": "90000",
            "fee": "1",
            "expiry": 1475903,
            "amt_to_forward_msat": "90000000",
            "fee_msat": "1250",
            "pub_key": "035639efb2bdd73ff6b82374a9d958c7ab404f8c1acb6dee678d9596e7cae25b2c"	
            })
            dataJson['routes'][0]["total_fees_msat"]=data["routes"][k]["total_fees_msat"] 
            dataJson['routes'][0]["total_amt_msat"]=data["routes"][k]["total_amt_msat"] 
    
    k=k+1
	
#to add an extra hop 
#dataJson['routes'][0]['hops'].append({
#	"chan_id": "1602118184053178368",
#    "chan_capacity": "500000",
#    "amt_to_forward": "90000",
#    "fee": "1",
#    "expiry": 1475903,
#    "amt_to_forward_msat": "90000000",
#    "fee_msat": "1250",
#    "pub_key": "035639efb2bdd73ff6b82374a9d958c7ab404f8c1acb6dee678d9596e7cae25b2c"	
#})



with open('route.json', 'w') as outfile:  
    json.dump(dataJson,outfile,indent=4)
	

with open('route.json') as f:
    dataPrint=json.loads(f.read())
	
print(dataPrint)

