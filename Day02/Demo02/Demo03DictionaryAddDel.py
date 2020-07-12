a = {'name':'单长喜','age':18,'job':'student'}
a["address"] = "山东省"
print(a)
a["name"] = "shanchance"
print(a)
b = {"age":22,"sex":"man"}
a.update(b)
print(a)

del(a["sex"])
print(a)
print(a.pop("address"))
print(a)
