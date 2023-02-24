import json 

#print(data1)
#Node under test 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 0270685ca81a8e4d4d01beec5781f4cc924684072ae52c507f8ebe9daf0caaab7b 03ee04b47f825c75db78c6e2fc56d0305eebed4451ccabb141a4102da9323b69e3 1600706411112235008 100000

#0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f

#Our chanel is open with 0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f

#Node 03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975


with open('Pointer.txt', 'r+') as pointer:
    p=pointer.read()

p=int(p)


if p==0:
    with open('testnet_graph.json', encoding="utf8") as f:
        data=json.loads(f.read())
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
    Channel_Data=json.loads(f.read())
	




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
    with open('data_test.json', encoding="utf8") as f:
        Channel_Data=json.loads(f.read())	
print(p)
print (capacity_cp)
print(choosed_peer)


	
#print(Channel_Data)