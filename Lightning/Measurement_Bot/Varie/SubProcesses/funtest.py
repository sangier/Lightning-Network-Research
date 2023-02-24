import subprocess 
import time


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
	 
	
