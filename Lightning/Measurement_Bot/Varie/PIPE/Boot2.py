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
address_only_pub="0260d9119979caedc570ada883ff614c6efb93f7f7382e25d73ecbeba0b62df2d7"
address="0260d9119979caedc570ada883ff614c6efb93f7f7382e25d73ecbeba0b62df2d7@88.99.209.230:9735"

			
#HERE if the channel has been already created jump to 3. 
#Step 2: Channel Creation 
#value=4200000
#value=1000000
#value=10000000
#cmd2="lncli -network=testnet openchannel "+address_only_pub+" "+str(value)

#if res==1 or res==0:
#    with open('Channel_Establishment_Log.txt', 'w+') as log2:
#        c = subprocess.Popen([cmd2], stdout=log2, stderr=log2, shell=True)
#        time.sleep(10)

#    res2=0		
#    with open('Channel_Establishment_Log.txt', 'r+') as f2:
#        now2=f2.read()
#        if now2.startswith("[lncli]"):
#            res2=-1
#            print("Channel Establishment failed:")
#            print(res2)
#            print(now2)
#        elif now2.startswith("{"):
#            res2=1
#            print("Channel Created!")
#            print(res2)
#            print(now2) 
#else:
#    print("There was a Connection Error")
	 

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
channel_temp=""
num_chan=(len(Channel_Data['channels']))

if p==num_chan:
    print("All channel have been tested")
    exit()	#shall we put this in a variable and analize this variable before proceding to query route steps.
else:
    for i in range(0,num_chan):
        print(i)
        if 	Channel_Data["channels"][p]["real_capacity"]==-1:
            if int(Channel_Data["channels"][p]["capacity"])>=4294967:	
                print("something")
                Channel_Data["channels"][p]["real_capacity"]=-2
            else:
                capacity_cp= int(Channel_Data["channels"][p]["capacity"])
                choosed_peer=Channel_Data["channels"][p]["node2_pub"]
                channel_temp=Channel_Data["channels"][p]["channel_id"]
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
capacity_test=capacity_cp
my_string=""
def_my_string=""



