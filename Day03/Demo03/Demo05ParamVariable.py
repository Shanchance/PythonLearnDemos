a = [10,20]
print(id(a))
print(a)

def test(m):
    print(id(m))
    print(m)
    m.append(300)
    print(id(m))

test(a)
print(a)