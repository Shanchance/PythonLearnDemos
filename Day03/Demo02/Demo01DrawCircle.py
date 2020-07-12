import turtle as t
color = ("red","green","blue","yellow","pink","grey","purple","Cyan")
t.speed(1)
t.width(5)
for i in range(50):

    t.color(color[i%8])
    t.circle(10+i*10)
    t.penup()
    t.goto(0, -i*10-10)
    t.pendown()

