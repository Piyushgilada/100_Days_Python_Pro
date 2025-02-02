import random
import turtle
from turtle import Turtle as t,Screen as s
gim=t()
gim.pencolor("black")
gim.shapesize(1.2)
direction=[0,90,180,270]
gim.pensize(5)
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for i in range(100):
    gim.pencolor(random_color())
    gim.forward(10)
    gim.setheading(random.choice(direction))
    gim.speed("fastest")

screen=s()
screen.exitonclick()
