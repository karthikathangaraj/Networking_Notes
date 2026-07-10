d1={
    "Name":"R1",
    "host": "192.1.1.1",
    "sys":"cicso",
     "Name":"kk",
     1:"sd",
     1:"kkkk",
     "list":[1,2,3,4],
     "t1":(1,2,3,4),
     "sets":{1,1,2,3,4,5},
     "dict":{1:12,2:22}
}
# print(d1) 

l1=[1,2,3,4]
l2=["a","b","c"]
d=dict(zip(l1,l2))
print(d)
print(d1.get("sets"))
d1["demo"]="python"

d1.update({
    "city":"chn",
    "cmpy":"IIT"
})
print(d1)
d1["list"].append(100)
print(d1["list"])
print(d1.keys())
print(d1.values()) 
del d1[1]
d1.popitem() 
print(d1)