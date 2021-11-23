human={'Name':"Adham","Age":20,3 :8,2:1}
print(human)
print(human["Name"])
print(human.get("Name"))
print(human.get("Na"))
human['Name']="ADDDDDDDD"
human.update({'Name':"Adham","Age":433,3 :5})
print(human)
del human[3]
inta =human.pop(2)
print(human,inta)
print(human.keys())
print(human.values())
print(human.items())
for key,value in human.items():
    print(key,value)