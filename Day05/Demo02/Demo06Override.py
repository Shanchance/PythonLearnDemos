class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  #私有属性
    def say_age(self):
        print("年龄：",self.__age)
    def say_introduce(self):
        print("姓名：",self.name)
class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score = score
    def say_age(self):
        print("方法重写了！！！")

s = Student("单长喜",22,100)
s.say_age()
s.say_introduce()