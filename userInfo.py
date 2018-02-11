import json

filename='userName.json'
info = {}

with open(filename) as f_obj:
    info=json.load(f_obj)

name=input('ur Name:')
pas=input('ur PassWord:')
info[name]=pas


with open(filename,'w') as f_obj:
    json.dump(info,f_obj)

for key,val in info.items():
    print("Name: "+key+"\nPassWords: "+val)

print("Count:"+str(len(info)))
