STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.speed("fast")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.lvl_map = 1
        
    def up(self):
        self.forward(10)
    
    def down(self):
        self.forward(-10)
        
    def goal(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.lvl_map += 1
            self.goto(STARTING_POSITION)
