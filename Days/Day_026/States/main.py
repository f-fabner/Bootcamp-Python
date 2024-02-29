import turtle
import pandas

screen = turtle.Screen()
screen.title("Brazil. States Game")
image = "N:\Programando\ProjetosGit\Bootcamp-Python\Days\Day_025\States\estados_em_branco.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_025/States/27_states.csv")
all_states = data.state.to_list()
guessed_states = []

#def get_mouse(x, y):
#    print(x, y)

#turtle.onscreenclick(get_mouse)
#turtle.mainloop()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_026/States/states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


'''
Mato Grosso do Sul 
Rio de Janeiro
Rio Grande do Norte
Rio Grande do Sul
I don't know why, but the 4 states above don't appear at all, I've already changed the coordinate, I've already checked the clicks, and nothing, these 4 still don't appear on the map after getting it right...
'''