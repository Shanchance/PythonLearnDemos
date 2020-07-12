class Person:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary  #私有属性
    def say_age(self):
        print("暂时不知道")

class Student(Person):
    def __init__(self,name,salary,score):
        Person.__init__(self,name,salary)
        self.score = score

student = Student("单长喜",18,100)
print(Student.mro())
print(student.score)
print(student._Person__salary)#私有属性
print(student.name)