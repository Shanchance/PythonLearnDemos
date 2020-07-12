"""
eval()函数，将函数内的字符串当做可执行有效表达式
"""

eval("print('hello world')")

a = 3
b = 4
c = eval("a+b")
print(c)