a = "姓名:{0}，年龄{1},{0}很帅"
print(a.format("单长喜",22))

b = "姓名:{name}，年龄{age},{name}很帅"
print(b.format(age=23,name="单长喜"))

c = "姓名:{name}，存款{money:.2f}"       #小数点保留两位小数
print(c.format(name="单长喜",money=3344.22222))