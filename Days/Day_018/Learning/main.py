from turtle import Turtle, Screen
from random import random, randint, choice

tim = Turtle()
tim.shape("turtle")
tim.color("DarkViolet")
tim.width(2)
tim.speed(30)

directions = [0, 90, 180, 270]


def random_color():
    return (random(), random(), random())

# for _ in range(4):
#    tim.forward(100)
#    tim.right(90)

# 169

# for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()


# 169
'''
tim.pencolor(random_color())
for _ in range(3):
    tim.forward(100)
    tim.right(120)

tim.pencolor(random_color())
for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.pencolor(random_color())
for _ in range(5):
    tim.forward(100)
    tim.right(72)
    
tim.pencolor(random_color())
for _ in range(6):
    tim.forward(100)
    tim.right(60)    

tim.pencolor(random_color())
for _ in range(7):
    tim.forward(100)
    tim.right(51.42)

tim.pencolor(random_color())
for _ in range(8):
    tim.forward(100)
    tim.right(45)

tim.pencolor(random_color())
for _ in range(9):
    tim.forward(100)
    tim.right(40)

tim.pencolor(random_color())
for _ in range(10):
    tim.forward(100)
    tim.right(36)
'''
# 170
'''
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.pencolor(random_color())
    draw_shape(shape_side_n)
'''
# 171
'''
for _ in range(100):
    angle = randint(0, 360)
    distance = randint(1, 50)
    tim.setheading(angle)
    tim.forward(distance)
'''
# 172
'''
for _ in range(100):
    direction = choice(directions)
    tim.setheading(direction)
    tim.forward(50)
    tim.pencolor(random_color())
'''
# 173
number_of_circles = 36
for _ in range(number_of_circles):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(10)


screen = Screen()
screen.exitonclick()
