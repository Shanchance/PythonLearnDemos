for x in (10,20,30):
    print(x**2)

for x in "abcde":
    print(x)

a = {"name":"shan","age":18,"address":"shandong"}
for i in a:
    print(i)
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)

evenNum = 0
oddNum = 0
sum = 0
for i in range(1,101):
    if i%2 == 0:
        evenNum+=i
    else:
        oddNum+=i
    sum+=i

print("1-100累计总和：{0}，奇数和：{1},偶数和：{2}".format(sum,oddNum,evenNum))
