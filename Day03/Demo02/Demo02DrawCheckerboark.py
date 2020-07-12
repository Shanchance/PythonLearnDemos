import turtle as t
from time import sleep

t.width(2)
t.speed(11)
for i in range(18):
    t.penup()
    t.goto(-85,170-i*10)
    t.pendown()
    t.goto(85,170-i*10)
    t.penup()

for i in range(18):
    t.penup()
    t.goto(-85+i*10,170)
    t.pendown()
    t.goto(-85+i*10,0)
    t.penup()
