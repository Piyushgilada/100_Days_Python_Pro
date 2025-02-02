from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

t = Turtle()
s = Screen()
b = Ball()
scoreboard=Scoreboard()

right_pedal =Paddle((370, 0))
left_pedal =Paddle((-380, 0))

s.setup(width=800, height=600)
s.title("Pong")
s.bgcolor("black")
s.tracer(0)

s.listen()
s.onkey(right_pedal.go_up, 'Up')
s.onkey(right_pedal.go_down, 'Down')
s.onkey(left_pedal.go_up, 'w')
s.onkey(left_pedal.go_down, 's')

game_is_on=True
while game_is_on:
    time.sleep(b.move_speed)
    s.update()
    b.random_move()

    # TODO detect collision with wall
    if b.ycor() > 280 or b.ycor() <-280:
        # need to bounce
        b.bounce_y()
    # TODO detect collision with pedal
    if b.distance(right_pedal) < 50 and b.xcor() > 340 or b.distance(left_pedal) < 50 and b.xcor() < -340:
        b.bounce_x()

    #TODO detect right/ left pedal missses the ball and score +1 to left
    if b.xcor()>380:
        b.reset_position()
        scoreboard.l_point()
    if b.xcor() < -380:
        b.reset_position()
        scoreboard.r_point()

s.exitonclick()
