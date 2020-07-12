s = (x*2 for x in range(5))
print(s)
print(tuple(s))

s = (x*2 for x in range(5))
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())

