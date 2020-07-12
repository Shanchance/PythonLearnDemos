class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if 0 < salary < 100000:
            self.__salary = salary
        else:
            print("录入错误！！")


e = Employee("单长喜",10000)
print(e.salary)
e.salary = 30000
print(e.salary)
