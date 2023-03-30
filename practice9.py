import turtle as t
import random as ran
from turtle import Screen
scr=Screen()
t.colormode(255)
t.pensize(2)
def color():
    r=ran.randint(0,255)
    g=ran.randint(0,255)
    b=ran.randint(0,255)
    rgbcolor=(r,g,b)
    return rgbcolor
for i in range(4):
    t.pencolor(color())
    t.forward(90)
    t.right(90)
    t.forward(90)
scr.exitonclick()