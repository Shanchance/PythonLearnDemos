a = " 圈子决定人生，接近什么样的人，就会走什么样的路，所谓物以类聚，人以群分。" \
    "牌友只会催你打牌，酒友只会催你干杯，而靠谱的人却会感染你如何取得进步。 "

print(len(a))       #长度

print(a.startswith("圈子"))       #以……为开头
print(a.startswith("不是"))       #以……为开头

print(a.endswith("进步。"))       #以……为结尾
print(a.endswith("不是"))         #以……为结尾

print(a.find("人"))              #第一次出现字符的位置
print(a.rfind("人"))             #最后一次出现字符的位置
print(a.count("人"))             #统计字符出现次数

print(a.isalnum())                  #是否全是字母或者数字
print("aaddbb4333".isalnum())       #是否全是字母或者数字

print(a.strip())                    #去除首尾空格
print("**ss*88*".strip("*"))        #去除首尾*号
print("**ss*88*".lstrip("*"))       #去除左边*号
print("**ss*88*".rstrip("*"))       #去除右边*号

print("=======================")

b = "i love you!"
c = "I loVe YoU!"
print(b.capitalize())       #整句首字母大写
print(b.upper())            #全部字母转为大写
print(b.title())            #全部单词首字母大写
print(c.lower())            #全部字母转为小写
print(c.swapcase())         #大写字母变成小写字母，小写变大写