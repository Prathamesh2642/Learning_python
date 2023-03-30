import turtle as t
from turtle import Screen
import random
t.colormode(255)
t.speed(speed=8)
t.pensize(5)
screen=Screen()

directions=[0,60,90,150,180,240,270,300,360]
def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
for i in range(500):
    t.setheading(random.choice(directions))
    t.pencolor(colors())
    t.forward(30)
screen.exitonclick()
