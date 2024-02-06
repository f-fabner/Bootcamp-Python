from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

'''
# my way...loooong and long way
tam = Turtle(shape="turtle")
tam.color("red")
tam.penup()
tam.goto(x=-230, y=-75)

tem = Turtle(shape="turtle")
tem.color("orange")
tem.penup()
tem.goto(x=-230, y=-45)

tim = Turtle(shape="turtle")
tim.color("yellow")
tim.penup()
tim.goto(x=-230, y=-15)

tom = Turtle(shape="turtle")
tom.color("green")
tom.penup()
tom.goto(x=-230, y=15)

tum = Turtle(shape="turtle")
tum.color("blue")
tum.penup()
tum.goto(x=-230, y=45)

sam = Turtle(shape="turtle")
sam.color("purple")
sam.penup()
sam.goto(x=-230, y=75)
'''

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color  == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
