"""
循环性能优化
"""

import time

start = time.time()

for i in range(1000):
    result = []
    for j in range(10000):
        result.append(i*1000+j*100)

end = time.time()
print("耗时：",end-start)

start = time.time()
for i in range(1000):
    result = []
    c = i *1000
    for j in range(10000):
        result.append(c+j*100)
end = time.time()
print("耗时：",end-start)