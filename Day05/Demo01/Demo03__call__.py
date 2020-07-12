#测试可调用方法__call__()

class SalaryCount:
    def __call__(self, salary):
        print("被调用了……")
        yearSalary = salary * 12
        monthSalary = salary
        daySalary = salary // 22.5
        hoursalary = daySalary // 24
        return dict(yearSalary = yearSalary,monthSalary=monthSalary,daySalary=daySalary,hoursalary=hoursalary)

s = SalaryCount()
print(s(3000))
