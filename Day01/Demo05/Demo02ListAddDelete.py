a = [1,2]
a.append(3)
print(a)
a.extend([4,5,6])
print(a)

a.insert(3,"shancx")
print(a)

a.remove("shancx")
print(a)
c = a.pop(5)
print(a)
del(a[3])
print(a)


b = a*3
print(b)