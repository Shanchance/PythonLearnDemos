import random

a = [1,4,2,5,7,4,5,6,9,3]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

random.shuffle(a)       #随机打乱顺序
print(a)
a.reverse()             #逆序
print(a)
print(max(a))           #最大值
print(min(a))           #最小值
print(sum(a))           #求和

