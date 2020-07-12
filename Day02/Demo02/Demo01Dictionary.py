a = {'name':'单长喜','age':18,'job':'student'}
print(a)
print(a['name'])
b = dict(name="单长喜",age=18)
print(b)
print(b['age'])
c = dict([('name','单长喜'),('age',18)])
print(c)
print(c['name'])
k = ["name","age","job"]
v = ["单长喜",18,"student"]
d = dict(zip(k,v))
print(d)
print(d["name"])
e = dict.fromkeys(["name","age","job"])
print(e)



