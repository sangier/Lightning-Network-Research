import json 
import subprocess
import time 
import os 
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome


#Global Variable: 
res=-1
address_only_pub=""
address=""
p=0
choosed_peer=""
capacity_cp=0
channel_temp=""
my_string=""
def_my_string=""
capacity_test=0
my_string=""
def_my_string=""
num_chan=0 
channel_direction=2
#oldtestnode:0260d9119979caedc570ada883ff614c6efb93f7f7382e25d73ecbeba0b62df2d7@88.99.209.230:9735
#newtestnode: 

def Connection_To_Peer():
#Step 1: Connection to target peer
    global p 
    global address_only_pub
    global address 
    p=0
    address_only_pub="02acb5b3bdf46d3a35e665c9abe46def12c341f55d603853ddeb1371076cab5c57"
    address="02acb5b3bdf46d3a35e665c9abe46def12c341f55d603853ddeb1371076cab5c57@68.183.221.146:49735"
    cmd="lncli -network=testnet connect "+address
    
    cmd_net="lncli -network=testnet describegraph >testnet_graph.json"
    c = subprocess.Popen([cmd_net],shell=True)
    time.sleep(10)
	
    with open('Connection_Log.txt', 'w+') as log:
        c = subprocess.Popen([cmd], stdout=log, stderr=log, shell=True)
        time.sleep(0.5)
   

def Channel_Establishment():
    #Step 2: Channel Creation 
    #value=4200000
    #value=1000000
    global p 
    global address_only_pub
    global address 
    value=4299000 
		   
    cmd2="lncli -network=testnet openchannel "+address_only_pub+" "+str(value)
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
            time.sleep(3600)			
        else:
            print("There was a Connection Error")

def Check_Channel_Establishment():
    			

def Retrieve_Channel(): 
#Step 3: Retrieve all channel owned by the target peer 
    global address_only_pub
    global num_chan
    with open('testnet_graph.json') as f:
        data=json.loads(f.read())
    dataJson={}
    dataJson['channels'] = []
    k=0
    for i in data["edges"]:
        if data["edges"][k]["node1_pub"]==address_only_pub:
            if data["edges"][k]["node1_policy"]!=None:
                if data["edges"][k]["node1_policy"]["disabled"]== 0:
                    if data["edges"][k]["node2_policy"]!=None:
                        if data["edges"][k]["node2_policy"]["disabled"]== 0:
                            dataJson['channels'].append({  
                        'node1_pub': data["edges"][k]["node1_pub"],
                        'node2_pub': data["edges"][k]["node2_pub"],
                        'channel_id': data["edges"][k]["channel_id"],
                        'capacity': data["edges"][k]["capacity"],
                        'real_capacity':-1,
                        'channel_direction':1
                })
        else:
            if data["edges"][k]["node2_pub"]==address_only_pub:
                if data["edges"][k]["node1_policy"]!=None:
                    if data["edges"][k]["node1_policy"]["disabled"]== 0:
                        if data["edges"][k]["node2_policy"]!=None:
                            if data["edges"][k]["node2_policy"]["disabled"]== 0:
                                dataJson['channels'].append({  
                            'node2_pub': data["edges"][k]["node1_pub"],
                            'node1_pub': data["edges"][k]["node2_pub"],
                            'channel_id': data["edges"][k]["channel_id"],
                            'capacity': data["edges"][k]["capacity"],
                            'real_capacity':-1,
                            'channel_direction':0
                })
        
        k=k+1
    with open('data_test.json', 'w') as outfile:  
        json.dump(dataJson,outfile,indent=4)
    with open('data_test.json') as f:
        Channel_Data=json.loads(f.read())
	#Step 4: Choose one of the available channels 
    num_chan=(len(Channel_Data['channels']))

def Choose_Channel():
    global p 
    global address_only_pub
    global address 
    global choosed_peer
    global capacity_cp
    global channel_temp
    global capacity_test
    global my_string
    global def_my_string
    global num_chan
    global channel_direction
    with open('data_test.json') as f:
        Channel_Data=json.loads(f.read())
	#Step 4: Choose one of the available channels 
    #num_chan=(len(Channel_Data['channels']))
    if p==num_chan:
        print("All channel have been tested")  #shall we put this in a variable and analize this variable before proceding to query route steps.
        Connection_To_Peer()
    else:
        for i in range(0,num_chan):
            print(i)
            if 	Channel_Data["channels"][p]["real_capacity"]==-1:
                if int(Channel_Data["channels"][p]["capacity"])>=4294967:	
                    print("Channel has a capacity too High")
                    Channel_Data["channels"][p]["real_capacity"]=-2
                else:
                    capacity_cp= int(Channel_Data["channels"][p]["capacity"])
                    choosed_peer=Channel_Data["channels"][p]["node2_pub"]
                    channel_temp=Channel_Data["channels"][p]["channel_id"]
                    channel_direction=Channel_Data["channels"][p]["channel_direction"]
                    p=p+1
                    break
            p=p+1
        with open('data_test.json', 'w') as outfile:  
            json.dump(Channel_Data,outfile,indent=4)
        with open('data_test.json') as f:
            Channel_Data=json.loads(f.read())	
    print(p)
    print (capacity_cp)
    print(choosed_peer)
    capacity_test=capacity_cp
    

	
	                                                                                                    
# lncli -network=testnet queryroutes 03e567bce8a40f5c36f6d431102290ad82cd99f9abca6b3f11aabcdd46f1d7bfcc 3999001 --final_cltv_delta=144
def Query_Select_Send_Routes(LambdaT):
#lncli -network=testnet queryroutes 03ce542ac3320900154ea33c8dfb0e8faa5e6facd88d5de22b011d135e3f5e906f 500000 --final_cltv_delta=144
#Step 5: Query Routes + Select Route 
    global address_only_pub
    global choosed_peer
    global capacity_test
    global my_string
    global def_my_string
    testFail=0
    cmd3="lncli -network=testnet queryroutes "+choosed_peer+" "+str(LambdaT)+" --final_cltv_delta=144"
    print(cmd3)
    with open('MyRoute.txt', 'w+') as log3:
        c = subprocess.Popen([cmd3], stdout=log3, stderr=log3, shell=True)
        time.sleep(10)
    with open('MyRoute.txt','r+') as test_log:
        l=test_log.read()
        if l.startswith("[lncli]"):
            testFail=1
            print("Capacity Test failed")
            return (testFail)
           
         				#ACTUALLY HERE IT HAS TO STOP THE EXECUTION AND GO BACK TO 1 Or Going back to channel choice. 
        else:			
                #HERE IT CAN HAPPEN THAT NO ROUTE IS PROVIDED --> IN THIS CASE IT MEANS THE TESTED CAPACITY IS NOT OK SO ANOTHER CONDITION OF FAILURE
            with open('MyRoute.txt') as f:
                data=json.loads(f.read())
                    
    dataJson={}

    dataJson['routes'] = []
    dataPrint=[]


#first hop : 0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f Previous: 038863cf8ab91046230f561cd5b386cbff8309fa02e3f0c3ed161a3aeb64a643b9
#second hoP: 03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975  Previous: 02fd753c8ad77d2601637b6add4362fec59f4d3e8190347ab4d155f3e9a76e113c
	
    k=0 
    j=0
    for i in data["routes"]:
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
                break
        
        k=k+1
    with open('route.json', 'w') as outfile:  
        json.dump(dataJson,outfile,indent=4)
        time.sleep(10)
			 
	#Timesleephere?
	data1=[]

    cmd4='lncli --network=testnet sendtoroute --payment_hash=35ac914ee69d4e30de1a12637fe49d3125ec0560b2b9af5d1b4cdf3884e87512 --routes="$(cat route.json)" -'

    with open('Payment_Attempt.json', 'w+') as log4:
        c = subprocess.Popen([cmd4], stdout=log4, stderr=log4, shell=True)
        time.sleep(15)

    with open('Payment_Attempt.json') as f:
        data=json.loads(f.read())

    k=0
    data1.insert(k,data["payment_error"])

    s = str(data1)
    substring1 = "unable to route payment to destination: " 
    my_string = s[(s.index(substring1)+len(substring1)):(len(s)-2)]
    if my_string=="UnknownNextPeer":
        testFail=0
        print(my_string)
        return (testFail)
    else: 
        substring1 = "ShortChannelID) "
        substring2 = " Timestamp"
        s1=s.index(substring1)+12
        s2=s.index(substring1)
        my_string = s[(s.index(substring1)+len(substring1)):s.index(substring2)]
        my_string=my_string[:-3]
        def_my_string=my_string
        testFail=1
        print(my_string)
        return (testFail)
	#capacity_test=(capacity_test)/10
    #if capacity_test <10: 
    #    break
#def SendToRoute():

def EstimateCapacity():
    global capacity_test
    inf="inf"
    epsilon=10
    reductionFactor=10
    IterationNum=5
    L=capacity_test
    Lt=0
    Lmax=0
    Lmin=0
    if(Query_Select_Send_Routes(L)==0):
        if(Query_Select_Send_Routes(L+epsilon)==0):
            return(L,inf)
        else:
            return(L,L)
    if(Query_Select_Send_Routes(epsilon)==1):
        return(0,epsilon)
    
    Lt=L/reductionFactor
    Lmax=L
    Lmin=0
    counter=0
    while(counter<IterationNum):
        if(Query_Select_Send_Routes(Lt)==0):
            Lmin=Lt
            Lt=(Lmax+Lmin)/2
        else:
            Lmax=Lt
            if(Lmin==0):
                Lt=Lt/reductionFactor
            else:
                Lt=(Lmax+Lmin)/2
        counter=counter+1
    
    return(Lmin,Lmax)	


    	
def Check_Channel(min,max):
    global def_my_string
    global channel_direction
    if def_my_string!="":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://1ml.com/testnet/")
        assert 'q' in driver.page_source
        action = action_chains.ActionChains(driver)
#action2=action_chains.ActionChains(driver)
#N.B. The execution of this 2 command before running this script is Mandatory. : 
# 1 :Xvfb -ac :99 -screen 0 1280x1024x16 &
# 2 :export DISPLAY=:99
# open up the developer console, mine on MAC, yours may be diff key combo
        print("blblblbl")
        print(def_my_string)
#time.sleep(3) '1480451:9:0'
        action.send_keys(def_my_string)
        action.send_keys(keys.Keys.ENTER)
        action.perform()
#time.sleep(3)


#to find the exact x path of an element: right click on the element -> analizza elemento -> right click -> copia -> Xpath 
        pageText = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/ul[2]/li[1]/div/a/h2").text

        print("From the webpage.. here the result: ")
        print(pageText)

        driver.close()


        if os.path.exists("data.json"):
            print("esiste fra")
            with open('data.json') as f:
                data=json.loads(f.read())
        else: 
            print("non esiste fra")
            data = {}  
            data['channels'] = []


        data['channels'].append({  
            'Node1_pub_key': address_only_pub,
            'Node2_pub_key': choosed_peer,
            'Channel_ID': pageText,
            'Short_Channel_ID': def_my_string,
            'Capacity': capacity_cp,
            'MinReal_Capacity': min,
            'MaxReal_Capacity': max,
            'Channel_direction': channel_direction,			
        })
    else:
        if os.path.exists("data.json"):
            print("esiste fra")
            with open('data.json') as f:
                data=json.loads(f.read())
        else: 
            print("non esiste fra")
            data = {}  
            data['channels'] = []
		
        data['channels'].append({  
            'Node1_pub_key': address_only_pub,
            'Node2_pub_key': choosed_peer,
            'Channel_ID': channel_temp,
            'Short_Channel_ID': def_my_string,
            'Capacity': capacity_cp,
            'MinReal_Capacity': min,
            'MaxReal_Capacity': max,
            'Channel_direction': channel_direction,			
        })

#iter(data).next()['edges'] = var
    with open('data.json', 'w') as outfile:  
        json.dump(data,outfile,indent=4)
        time.sleep(10)


#Main: 
def Main():
    global res
    global address_only_pub
    global address
    global p
    global choosed_peer
    global capacity_cp
    global channel_temp
    global my_string
    global def_my_string
    global capacity_test
    global my_string
    global def_my_string
    global num_chan
    global channel_direction
    Connection_To_Peer()
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
    if res==1:
        Channel_Establishment()
    
    Retrieve_Channel()
    time.sleep(10)
    print(p,num_chan)
    while (p<num_chan):
        Choose_Channel()
        
        min, max = EstimateCapacity()
        print("IL RISULTATO DEL TEST E':")
        print(min,max)
        Check_Channel(min,max)
        print("Esecuzione Numeroooo:")
        print(p)
        def_my_string=""
        with open('data.json') as f:
            dataPrint=json.loads(f.read())
            print(dataPrint)
            print(num_chan,p)
            if(p==num_chan -1):
                break
	
	
Main()
