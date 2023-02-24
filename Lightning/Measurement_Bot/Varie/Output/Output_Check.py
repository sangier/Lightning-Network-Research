import json 
import subprocess
import time 


data1=[]

cmd4='lncli --network=testnet sendtoroute --payment_hash=35ac914ee69d4e30de1a12637fe49d3125ec0560b2b9af5d1b4cdf3884e87512 --routes="$(cat route.json)" -'

with open('Payment_Attempt.json', 'w+') as log4:
    c = subprocess.Popen([cmd4], stdout=log4, stderr=log4, shell=True)
    time.sleep(10)

with open('Payment_Attempt.json') as f:
    data=json.loads(f.read())

k=0
data1.insert(k,data["payment_error"])

s = str(data1)
substring1 = "unable to route payment to destination: " 
my_string = s[(s.index(substring1)+len(substring1)):(len(s)-2)]
if my_string=="UnknownNextPeer":
    print(my_string)
else: 
    substring1 = "ShortChannelID) "
    substring2 = " Timestamp"
    s1=s.index(substring1)+12
    s2=s.index(substring1)
    my_string = s[(s.index(substring1)+len(substring1)):s.index(substring2)]
    my_string=my_string[:-3]
    print(my_string)