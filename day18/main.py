import random
from turtle import Turtle as t,Screen as s
gim=t()
gim.color("red")
gim.pencolor("black")
gim.shapesize(1.2)
color=["black", "red","brown","blue"]
user_want=int(input("how may side you want"))
side = 3
for i in range(user_want-1):
    gim.pencolor(random.choice(color))
    angle = round(360 / side)
    for c in range(side):
        gim.forward(20)
        gim.right(angle)
    side=side+1



screen=s()
screen.exitonclick()

