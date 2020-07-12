class MySingleton:
    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
            return cls.__obj
    def __init__(self,name):
        if MySingleton.__init_flag:
            print("init……")
            self.name = name
            MySingleton.__init_flag = False

a = MySingleton("AA")
b = MySingleton("BB")
print(a)
print(b)