a = [
        ["单一",18,20000,"北京"],
        ["单二",19,30000,"上海"],
        ["单三",20,40000,"深圳"]
    ]

print(a)
print(a[0])
print(a[0][0])

for i in range(3):
    for j in range(4):
        print(a[i][j],end="\t")
    print(end="\n")