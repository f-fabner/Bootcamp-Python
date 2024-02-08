from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PonG!")
screen.tracer(0)

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 278 or ball.ycor() < -278:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.gol()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.gol()
        scoreboard.r_point()


screen.exitonclick()
