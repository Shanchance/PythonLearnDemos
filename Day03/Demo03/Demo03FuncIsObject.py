def test():
    print("This is a function")

test()
c = test
c()
print(id(test))
print(id(c))
print(type(c))