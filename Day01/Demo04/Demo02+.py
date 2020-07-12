import time

time01 = time.time()
a = ""
for i in range(1000000):
    a+="sxt"

time02 = time.time()
print("运算时间："+str(time02-time01))

time03 = time.time()
b = []
for i in range(1000000):
    b.append("sxt")
"".join(b)
time04 = time.time()
print("运算时间："+str(time04-time03))