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
        c = subprocess.Popen(["python Boot.py"], shell=True)
        c.wait()
        time.sleep(0.5)
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
            c = subprocess.Popen(["python Boot.py"], shell=True)
            c.wait()			
