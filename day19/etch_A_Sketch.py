from turtle import Turtle,Screen

tim=Turtle()
s=Screen()
def move_forward():
    tim.forward(20)

def move_backward():
    tim.left(180)
    tim.forward(20)

def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)

def clear():
    tim.reset()
def undo():
    tim.undo()

s.listen()
s.onkey(key='w',fun=move_forward)
s.onkey(key='s',fun=move_backward)
s.onkey(key='a',fun=counter_clockwise)
s.onkey(key='d',fun=clockwise)
s.onkey(key='space',fun=undo)
s.onkey(key='c',fun=clear)

s.exitonclick()