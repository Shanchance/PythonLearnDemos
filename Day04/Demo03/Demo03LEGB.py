#测试LEGB规则

#str = "global"
def outer():
    #str = "outer"
    def inner():
        #str = "inner"
        print(str)
    inner()
outer()