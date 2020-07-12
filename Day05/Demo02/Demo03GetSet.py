class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 0<salary<100000:
            self.__salary = salary
        else:
            print("录入错误！！")

e = Employee("单长喜",30000)
print(e.get_salary())
e.set_salary(50000)
print(e.get_salary())