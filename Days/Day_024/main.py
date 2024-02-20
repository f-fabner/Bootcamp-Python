from turtle import Screen
from kroba import Kroba
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da KROBA!")
screen.tracer(0)

kroba = Kroba()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(kroba.up, "Up")
screen.onkey(kroba.down, "Down")
screen.onkey(kroba.left, "Left")
screen.onkey(kroba.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    kroba.move()

    # Detect collision with food
    if kroba.head.distance(food) < 15:
        food.refresh()
        kroba.extend()
        score.increase_score()

    # Detect collision with wall.
    if kroba.head.xcor() > 285 or kroba.head.xcor() < -285 or kroba.head.ycor() > 285 or kroba.head.ycor() < -285:
        score.reset()
        kroba.reset()
        
    # Detect collision with tail
    for segment in kroba.segments[1:]:
        if kroba.head.distance(segment) < 10:
            score.reset()
            kroba.reset()

screen.exitonclick()
