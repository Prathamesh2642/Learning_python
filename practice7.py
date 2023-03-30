from turtle import Turtle,Screen
import random as ran
t=Turtle()
screen=Screen()
sides=int(input("Enter number of sides"))
def colors():
    r=ran.randint(0,255)
    g=ran.randint(0,255)
    b=ran.randint(0,255)
    return (r,g,b)
t.pencolor("red")
def shape(sides):
    for i in range(sides):
        t.forward(70)
        t.left(360/sides)
for i in range(4,10):
    t.color(colors())
    shape(i)
print(t.position())
screen.exitonclick()