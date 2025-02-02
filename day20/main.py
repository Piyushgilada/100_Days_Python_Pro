from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake_object=Snake()
food_object=Food()
score_object=Scoreboard()

s.listen()
s.onkey(snake_object.up, "Up")
s.onkey(snake_object.down, "Down")
s.onkey(snake_object.left, "Left")
s.onkey(snake_object.right, "Right")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake_object.move()
    # TODO detect collision with food
    if snake_object.head.distance(food_object)< 15:
        food_object.refresh()
        snake_object.extend()
        score_object.increase_score()

    # TODO detect wall collision
    if snake_object.head.xcor() > 280 or snake_object.head.xcor() < -280 or snake_object.head.ycor() > 280 or snake_object.head.ycor() < -280:
        score_object.reset_method()
        snake_object.reset()

    # TODO detect collision with tail
    for seg in snake_object.segments[1:-1:1]:
        if snake_object.head.distance(seg)<10:
        # if seg!=snake.head and snake.head.distance(seg)<10:
            score_object.reset_method()
            snake_object.reset()

s.exitonclick()
