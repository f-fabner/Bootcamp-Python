from tkinter import *
import math
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def button_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="TIMER")
    label_checkmark.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- #


def button_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text=" Break! ", fg=RED, bg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text=" Break! ", fg=PINK, bg=VIOLET)

    else:
        count_down(work_sec)
        label_title.config(text=" Work! ", fg=GREEN, bg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        button_start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LILAC)

# label tomato
canvas = Canvas(width=200, height=224, bg=LILAC, highlightthickness=0)
tomato_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_028/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill=VIOLET,
                                font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# label title
label_title = Label(text="TIMER", font=(
    FONT_NAME, 40, "bold"), fg=GREEN, bg=LILAC)
label_title.grid(column=1, row=0)

# label checkmark
label_checkmark = Label(font=(FONT_NAME, 26, "bold"), fg=GREEN, bg=LILAC)
label_checkmark.grid(column=1, row=3)

# Button 01(start)
start_button = Button(text="Start", command=button_start)
start_button.grid(column=0, row=2)

# Button 02(reset)
reset_button = Button(text="Reset", command=button_reset)
reset_button.grid(column=2, row=2)

window.mainloop()
