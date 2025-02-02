# import colorgram
# colors = colorgram.extract('1234.jpg', 30)
# rgb_colors=[]
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_colors=(r,g,b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle ,Screen
turtle.colormode(255)
color_palllet = [(235, 228, 211), (217, 218, 223), (104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32),
                     (225, 212, 109), (199, 147, 173), (237, 215, 225), (105, 112, 170), (177, 159, 47),
                     (218, 224, 219),
                     (186, 19, 9), (38, 40, 21), (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101),
                     (205, 87, 58),
                     (58, 68, 54), (132, 136, 132), (190, 187, 218), (230, 176, 172), (231, 65, 82)]
turtle.bgcolor("black")
gim=Turtle()
gim.penup()
gim.setheading(225)
gim.forward(300)
gim.setheading(0)
number_of_dots=100
gim.speed("fastest")
for dot_count in range(1,number_of_dots+1):
    gim.dot(20,random.choice(color_palllet))
    gim.forward(50)
    if dot_count %10 ==0:
        gim.setheading(90)
        gim.forward(50)
        gim.setheading(180)
        gim.forward(500)
        gim.setheading(0)

gim.hideturtle()
s=Screen()
s.exitonclick()