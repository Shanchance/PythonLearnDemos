"""
绘制一个折线，求起始点到终点的距离
"""
import math
import turtle as t

def drawLine():
    x1,y1=100,100
    x2,y2=100,-100
    x3,y3=-100,-100
    x4,y4=-100,100
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)

    distance = math.sqrt((x1-x4)**2+(y1-y4)**2)
    t.write(distance)

drawLine()
