'''
import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkViolet")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
'''
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

#how teacher does:
#table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
#table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)