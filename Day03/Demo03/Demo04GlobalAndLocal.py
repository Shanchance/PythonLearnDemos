a = 5           #全局变量
def test():
    b = 4       #局部变量

    global a
    a=7080
    print(a)

    print(b*10)
    print(id(b))
test()

