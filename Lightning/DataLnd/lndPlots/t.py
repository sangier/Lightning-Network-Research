import json 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


with open('p.json') as f:
    closing=json.loads(f.read())
	
	
if( len(closing["waiting_close_channels"])!=0  or len(closing["pending_closing_channels"])!=0): #HERE YOU HAVE TO ADD THE FORCE PENDING CONTROL
    print(closing["waiting_close_channels"],closing["pending_closing_channels"])
    print("We have to wait 12 minutes to check again the channel closing")
else:
    print(closing["waiting_close_channels"],closing["pending_closing_channels"])
    print("Channel to peer successfully closed")			


#print(x)