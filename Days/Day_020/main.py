from turtle import Screen
from kroba import Kroba
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da KROBA!")
screen.tracer(0)

kroba = Kroba()

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


screen.exitonclick()
