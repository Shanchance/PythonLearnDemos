#列表推导式
y = [x*2 for x in range(1,5)]
print(y)

cell = [(row,col) for row in range(10) for col in range(10)]
print(cell)


#字典推导式
text = "i love China, i love ShanDong, i love myself"
d = {c:text.count(c) for c in text}
print(d)
print("===========另一种普通方法===========")
dict = {}
for c in text:
    dict[c] = text.count(c)

print(dict)

#集合推导式

a = {x for x in range(100) if x%5 ==0}
print(a)

#生成器推导式
#生成器只能使用一次
generator = (x for x in range(5))
print(generator)
print(tuple(generator))
print(tuple(generator))

gen = (x for x in range(5))
for i in gen:
    print(i,end="\t")
print(tuple(gen))