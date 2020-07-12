class Person:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}——{1}".format(self.name,other.name)
        else:
            return "不是同类不可以相加"

p1 = Person("单长喜")
p2 = Person("于潇潇")
x = p1+p2
print(x)