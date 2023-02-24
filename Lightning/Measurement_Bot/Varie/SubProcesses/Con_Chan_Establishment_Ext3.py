import subprocess 
import time

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

#the describegraph command when should  be exectued? At the beginning one time or Every time at this step? 

with open('testnet_graph.json', encoding="utf8") as f:
    data=json.loads(f.read())

#Node under test 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 0270685ca81a8e4d4d01beec5781f4cc924684072ae52c507f8ebe9daf0caaab7b 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 1600706411112235008 100000

#0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f

#Our chanel is open with 0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f

#Node 03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975

dataJson={}

dataJson['channels'] = []

k=0
for i in data["edges"]:
    if data["edges"][k]["node1_pub"]=="0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f":
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
	

with open('data_test.json', encoding="utf8") as f:
    dataPrint=json.loads(f.read())
	
print(dataPrint)
	 
