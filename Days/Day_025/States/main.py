import turtle
import pandas as pd

def move_turtle(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

screen = turtle.Screen()
screen.title("Brazil States Game!")
image = "N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_025/States/estados_em_branco.gif"
screen.addshape(image)
turtle.shape(image)



'''
def click_coor(x, y):
    print(x, y)
    
turtle.onscreenclick(click_coor)

turtle.mainloop()
'''
file_path = "N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_025/States/27_states.csv"
states_data = pd.read_csv(file_path)

total_states = len(states_data)
correct_guesses = 0

game_is_on = True

while correct_guesses < total_states:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()

    if answer_state.lower() == "exit":
        break  
    
    if answer_state in states_data["state"].values:
        state_info = states_data[states_data["state"] == answer_state].iloc[0]
        x, y = state_info["x"], state_info["y"]

        move_turtle(x, y)
        turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))
        correct_guesses += 1


screen.exitonclick()
