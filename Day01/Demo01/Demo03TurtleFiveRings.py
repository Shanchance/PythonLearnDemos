import time
import turtle as t

def drawFiveRings():
    t.width(10)
    t.penup()
    t.goto(-120,0)
    t.pendown()
    t.color("blue")
    t.circle(50)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color("black")
    t.circle(50)
    t.penup()
    t.goto(120,0)
    t.pendown()
    t.color("red")
    t.circle(50)
    t.penup()
    t.goto(-60,-40)
    t.pendown()
    t.color("yellow")
    t.circle(50)
    t.penup()
    t.goto(60,-40)
    t.pendown()
    t.color("green")
    t.circle(50)
    time.sleep(20)#睡眠

drawFiveRings()
