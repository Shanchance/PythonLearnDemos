t1 = {"name":"单一","age":19,"city":"北京"}
t2 = {"name":"单二","age":20,"city":"上海"}
t3 = {"name":"单二","age":21,"city":"深圳"}

tb = [t1,t2,t3]
print(tb)
print(tb[1].get("age"))         #第二行人的年龄
for i in range(3):              #打印所有的城市
    print(tb[i].get("city"))

for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),tb[i].get("city"))

