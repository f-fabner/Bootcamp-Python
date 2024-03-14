from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv(
    "N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_031/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(
    "N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_031/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# ************************DEFS************************


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card_img)


def know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_031/data/words_to_learn.csv", index=False)
    next_card()

# ************************UI************************


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(height=526, width=800)
front_card_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_031/images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

back_card_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_031/images/card_back.png")
right_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_031/images/right.png")
wrong_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_031/images/wrong.png")


# ************************BUTTONS************************
# Button right
button_right = Button(image=right_img, highlightthickness=0, command=know)
button_right.grid(column=1, row=1)
# Button wrong
button_wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)

next_card()

window.mainloop()
