class Employee:
    @property
    def salary(self):
        print("运行了……")
        return 10000
e = Employee()
#e.salary
print(e.salary)