a = [10,20,30,20,40,10,50,80]

print(a[2])
print(a.index(20))
print(a.index(20,2,5))
print(a.count(20))

print(20 in a)
print(20 not in a)

b = a[1:5:2]
print(b)
c = a[-3:]
print(c)

for i in a:
    print(i,end=" ")

