import json 
import pandas as pd 

data=pd.read_json("Comparison.json")

dataFiltered = {}  
dataFiltered['channels'] = []


todo=0
nada=0
mix=0
NumChane=len(data)


df2_outOk=data[(data["Balance"]==0) & (data["Channel_directionPeer1"]==1)]
print(len(df2_outOk))

df2_inOk=data[(data["Balance"]==0) & (data["Channel_directionPeer1"]==0)]
print(len(df2_inOk))

sum0=len(df2_outOk)+len(df2_inOk)

df2_midOut=data[(abs(data["Balance"])<10*data["Capacity"]/100) & (data["Channel_directionPeer1"]==1) & (data["Balance"]!=0)]
print(len(df2_midOut))

df2_midIn=data[(abs(data["Balance"])<10*data["Capacity"]/100) & (data["Channel_directionPeer1"]==0) & (data["Balance"]!=0)]
print(len(df2_midIn))

sum1=len(df2_midOut)+len(df2_midIn)

df2_VarOut=data[(abs(data["Balance"])>10*data["Capacity"]/100) & (data["Channel_directionPeer1"]==1) & (data["Balance"]!=0)]
print(len(df2_VarOut))

df2_VarIn=data[(abs(data["Balance"])>10*data["Capacity"]/100) & (data["Channel_directionPeer1"]==0) & (data["Balance"]!=0)]
print(len(df2_VarIn))

sum2=len(df2_VarOut)+len(df2_VarIn)


print("Mixed InOut Stats: ")
print("ChannelPerfectlyMeasured: "+str(sum0)+" -->"+str(sum0/NumChane))

print("ChannelWithHighVariation: "+str(sum2)+" -->"+str(sum2/NumChane))
print("ChannelWithVariation%Error: "+str(sum1)+" -->"+str(sum1/NumChane))


print("In Stats: ")
print("ChannelPerfectlyMeasuredIn: "+str(len(df2_inOk))+" -->"+str(len(df2_inOk)/NumChane))
print("ChannelWithHighVariationIn: "+str(len(df2_VarIn))+" -->"+str(len(df2_VarIn)/NumChane))
print("ChannelErrorVariationIN: "+str(len(df2_midIn))+" -->"+str(len(df2_midIn)/NumChane))


print("Out Stats: ")
print("ChannelWithHighVariationOut: "+str(len(df2_VarOut))+" -->"+str(len(df2_VarOut)/NumChane))

print("ChannelErrorVariationOut: "+str(len(df2_midOut))+" -->"+str(len(df2_midOut)/NumChane))
print("ChannelPerfectlyMeasuredOut: "+str(len(df2_outOk))+" -->"+str(len(df2_outOk)/NumChane))
