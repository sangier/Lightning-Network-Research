from blockchain import blockexplorer
import json 
import pandas as pd 
import os 

num_chan=0


with open('mainnet_red_graph.json',encoding='utf-8') as f:
    data=json.loads(f.read())

Channels={}
Channels=data["edges"]
AliveChannels={}
AliveChannels["edges"]=[]

with open('AliveChannels.json', 'a') as outfile:  
    json.dump(AliveChannels,outfile,indent=4)
FundingValueCheck={}
FundingValueCheck['edges']=[]
with open('FundingValueCheck.json', 'a') as outfile:  
    json.dump(FundingValueCheck,outfile,indent=4)


print(len(Channels))

#len(Channels)
k=18493
j=0
for i in range(18493,len(Channels)):
    funding=Channels[k]["chan_point"]
    TxOut=funding[65:90]
    TxOut=int(TxOut.split(" ")[0])
    funding=funding[:64]
    print(funding,TxOut)
    Tx=blockexplorer.get_tx(funding)
    if(len(Tx.outputs)>=2):
        TxOut=1
    else:
        TxOut=0
    if(TxOut==1):
        if(int(Channels[k]["capacity"])==int(Tx.outputs[TxOut].value)):
            value=int(Tx.outputs[TxOut].value)
            TxOut=1
        elif(int(Channels[k]["capacity"])==int(Tx.outputs[0].value)):
            TxOut=0    
    print(len(Tx.outputs))
    r=Tx.outputs[TxOut].spent
    if(r==False):
        with open('AliveChannels.json', 'a') as outfile:  
            json.dump(Channels[k],outfile,indent=4,)
        match=0
        value=0
        if(int(Channels[k]["capacity"])==int(Tx.outputs[TxOut].value)):
            value=int(Tx.outputs[TxOut].value)
            match=1
        else:
            if(TxOut==1):
                if(int(Channels[k]["capacity"])==int(Tx.outputs[TxOut-1].value)): 
                    value=int(Tx.outputs[TxOut-1].value)
                    match=1
        FundingValueCheck['edges'].append({  
            'node1_pub_key': Channels[k]["node1_pub"],
            'node2_pub_key': Channels[k]["node2_pub"],
            'channel_ID': Channels[k]["channel_id"],
            'capacity': Channels[k]["capacity"],
            'TxHash': funding,
            'FTxValue': value,
            'Match': match,			
            })
        with open('FundingValueCheck.json', 'a') as outfile:  
            json.dump(FundingValueCheck["edges"][j],outfile,indent=4)
        j=j+1
    k=k+1
    print(k,r)	

# output = []
# for f in files:
    # # ...
    # output.append(data)   },\n{\n    "channel_id"
# json.dump(output, outfile)

