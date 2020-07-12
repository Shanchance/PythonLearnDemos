class Test:
    def __init__(self,name,age):
        self.name = name
        self.__age = age        #私有属性
    def __fun(self):
        print("好好学习")

test = Test("单长喜",18)
print(test.name)
#print(test.age)
print(test._Test__age)
test._Test__fun()