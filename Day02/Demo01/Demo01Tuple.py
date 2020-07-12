"""
元组的元素不可更改
"""

a = (1,3,2,7,4,5,6)
print(type(a))
print(a[0])
#  a[0] = 100 元组的元素不可更改
print(sorted(a))
b = (1)
print(type(b))
c = (1,)
print(type(c))
d = tuple("shanchance")
print(d)
print(d[1:3])
print(d[::-1])
print(tuple(range(10)))
print(tuple([1,2,3]))