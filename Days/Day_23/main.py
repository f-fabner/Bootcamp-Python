import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    turtle.goal()
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect Collision
    for each_car in car_manager.all_cars:
        if each_car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    #detect goal
    if turtle.ycor() > 250:
        car_manager.level_up()
        scoreboard.lvl_up()

screen.exitonclick()
