import random
import turtle
from turtle import Turtle,Screen
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(tim)

s=Screen()
s.setup(500,400)
user_bet=s.textinput("make your bet","what color of turtle which is going to win ?")
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            if winner==user_bet:
                print(f"user won the bet with {winner} turtle")
            else:
                print(f"user lost the bet winner is {winner} turtle")
        ran_distance=random.randint(0,10)
        turtle.forward(ran_distance)
s.exitonclick()