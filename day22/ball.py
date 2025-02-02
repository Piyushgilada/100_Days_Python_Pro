from turtle import Turtle,Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_speed=0.1
        self.x_move=10
        self.y_move=10

    def random_move(self):
        x_ran=self.xcor()+self.x_move
        y_ran=self.ycor()+self.y_move
        self.goto(x_ran,y_ran)

    def bounce_y(self):
        self.y_move*=-1
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed*=0.9
