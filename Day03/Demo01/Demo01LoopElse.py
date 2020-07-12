"""
测试循环中else
"""

salarys = []
sumSalary = 0
for i in range(4):
    s = input("请输入一共四名员工的工资（按Q或者q退出）")
    if s.upper() == 'Q':
        break
    if float(s) < 0:
        continue
    salarys.append(float(s))
    sumSalary+=float(s)
else:
    print("您已经全部录入四名员工的工资")

print("录入工资：",salarys)
print("平均工资：",sumSalary/4)
