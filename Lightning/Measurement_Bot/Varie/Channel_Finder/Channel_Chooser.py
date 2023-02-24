import json 

with open('data_test.json', encoding="utf8") as f:
    Channel_Data=json.loads(f.read())
	
with open('Pointer.txt', 'r+') as pointer:
    p=pointer.read()

p=int(p)


choosed_peer=""
capacity_cp=0

num_chan=(len(Channel_Data['channels']))

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
	
print(p)
print (capacity_cp)
print(choosed_peer)

with open('data_test.json', 'w') as outfile:  
    json.dump(Channel_Data,outfile,indent=4)
	

with open('data_test.json', encoding="utf8") as f:
    Channel_Data=json.loads(f.read())
	
print(Channel_Data)

#if data["edges"][k]["node1_pub"]=="0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f":
#        if data["edges"][k]["node1_policy"]["disabled"]== 0:
#            if data["edges"][k]["node2_policy"]["disabled"]== 0:
#                dataJson['channels'].append({  
#            'node1_pub': data["edges"][k]["node1_pub"],
#            'node2_pub': data["edges"][k]["node2_pub"],
#            'channel_id': data["edges"][k]["channel_id"],
#			'capacity': data["edges"][k]["capacity"],
#			'real_capacity':-1,