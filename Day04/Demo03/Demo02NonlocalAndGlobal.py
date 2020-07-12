#测试nonlocal,global 关键字
def outer():
    b =20
    def inner():
        nonlocal b      #声明外层局部变量
        print(b)
        b = 30
        print(b)
    inner()
    print(b)
outer()