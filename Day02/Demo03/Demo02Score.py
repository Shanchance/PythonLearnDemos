score = int(input("请输入一个0-100之间的分数"))
degree = "ABCDE"
num = score//10
if score>100 or score<0:
    print("分数范围有误，请重新输入")
else:
    if num<6:
        num = 5
    elif num==10:
        num = 9
    print("分数是{0}，等级是{1}".format(score,degree[9-num]))
