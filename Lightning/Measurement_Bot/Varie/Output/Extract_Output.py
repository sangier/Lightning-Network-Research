import json 



with open('output2.json', encoding="utf8") as f:
    data=json.loads(f.read())

data1=[]

k=0
data1.insert(k,data["payment_error"])

s = str(data1)
substring1 = "unable to route payment to destination: " 
my_string = s[(s.index(substring1)+len(substring1)):(len(s)-2)]
print(my_string)
