import json 

with open('output.json', encoding="utf8") as f:
    data=json.loads(f.read())

data1=[]


k=0
data1.insert(k,data["payment_error"])
s = str(data1)
substring1 = "ShortChannelID) "
substring2 = " Timestamp"
s1=s.index(substring1)+12
s2=s.index(substring1)
my_string = s[(s.index(substring1)+len(substring1)):s.index(substring2)]
my_string=my_string[:-3]
print(my_string)
