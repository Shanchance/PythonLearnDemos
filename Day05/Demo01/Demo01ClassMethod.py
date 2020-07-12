#测试类方法，静态方法
class Student:
    company = "SXT"         #类属性
    @classmethod
    def printCompany(cls):
        print(cls.company)
Student.printCompany()


class Student2:
    company = "SXT"         #类属性
    @staticmethod
    def add(a,b):
        print("{0}+{1}={2}".format(a,b,a+b))

Student2.add(4,6)



