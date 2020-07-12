
f = lambda a,b,c,d:a*b*c*d
print(f(3,4,5,6))

f2 = [lambda a:a*2,lambda b:b*10]
print(f2[1](3))
