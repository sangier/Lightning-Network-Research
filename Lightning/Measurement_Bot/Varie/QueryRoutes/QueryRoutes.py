import json 

address_only_pub="0260d9119979caedc570ada883ff614c6efb93f7f7382e25d73ecbeba0b62df2d7"

#address_only_pub="0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f"
#choosed_peer="03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975"
choosed_peer="030f375d8aecdddc852309c15c3b67c2934de0de4d31e1e04a03d656ca0a78d008"
capacity_cp=900000


cmd3="lncli -network=testnet queryroutes "+choosed_peer+" "+capacity_cp+" --final_cltv_delta=144"
with open('MyRoute.json', 'w+') as log3:
    c = subprocess.Popen([cmd3], stdout=log3, stderr=log3, shell=True)
    time.sleep(10)

with open('MyRoute.json') as f:
    data=json.loads(f.read())

dataJson={}

dataJson['routes'] = []
dataPrint=[]

lncli --network=testnet sendtoroute --payment_hash=35ac914ee69d4e30de1a12637fe49d3125ec0560b2b9af5d1b4cdf3884e87512 --routes="$(cat route.json)" -
#first hop : 0269a94e8b32c005e4336bfb743c08a6e9beb13d940d57c479d95c8e687ccbdb9f Previous: 038863cf8ab91046230f561cd5b386cbff8309fa02e3f0c3ed161a3aeb64a643b9
#second hoP: 03ecd95e86e780ae82139c3217b527073622d28c4d8a53b76142a7b7b1d1e36975  Previous: 02fd753c8ad77d2601637b6add4362fec59f4d3e8190347ab4d155f3e9a76e113c
	
k=0 
j=0
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
	

with open('route.json', encoding="utf8") as f:
    dataPrint=json.loads(f.read())
	
print(dataPrint)