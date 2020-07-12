def test(a,b):
    c = a+b
    sum = 0
    for i in range(20):
        sum+=1
    return c,sum

print("3 + 4 =",test(3,4))
