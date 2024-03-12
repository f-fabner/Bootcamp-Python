from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
LILAC = "#d68dfc"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
VIOLET = "#4c0075"

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def button_reset():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- #
def button_start():
    pass
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LILAC)

#label tomato
canvas = Canvas(width=200, height=224, bg=LILAC, highlightthickness=0)
tomato_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_028/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 135, text="00:00", fill=VIOLET,
                   font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

#label title
label_title = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=LILAC)
label_title.grid(column=1, row=0)

#label checkmark
label_checkmark = Label(text="✓", font=(FONT_NAME, 26, "bold"), fg=GREEN, bg=LILAC)
label_checkmark.grid(column=1, row=3)

# Button 01(start)
button = Button(text="Start", command=button_start)
button.grid(column=0, row=2)

# Button 02(reset)
button = Button(text="Reset", command=button_reset)
button.grid(column=2, row=2)

window.mainloop()
