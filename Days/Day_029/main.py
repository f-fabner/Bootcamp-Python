from tkinter import *
LILAC = "#d68dfc"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #


def buttonadd():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=LILAC)

# label padlock
canvas = Canvas(height=200, width=200, bg=LILAC, highlightthickness=0)
padlock_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_029/logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0, padx=(0, 100))

# Label website
web_label = Label(text="Website:", bg=LILAC)
web_label.grid(column=0, row=1, padx=(10, 0))

# Label Email/Username
id_label = Label(text="Email/Username:", bg=LILAC)
id_label.grid(column=0, row=2, padx=(10, 0))

# Label Password
pass_label = Label(text="Password:", bg=LILAC)
pass_label.grid(column=0, row=3, padx=(10, 0))

# Entry website
input_site = Entry(width=45)
input_site.grid(column=1, row=1, columnspan=2, padx=(0, 100))

# Entry email/username
input_id = Entry(width=45)
input_id.grid(column=1, row=2, columnspan=2, padx=(0, 100))

# Entry blank
generated_password = Entry(width=20)
generated_password.grid(column=1, row=3, padx=(0, 250))

# Button Generate
button_generate_password = Button(
    width=18, text="Generate Password", command=generate)
button_generate_password.grid(column=1, row=3, padx=(20, 0))
# Button ADD
button_add = Button(width=36, text="Add", command=buttonadd)
button_add.grid(column=0, row=4, columnspan=3)

window.mainloop()
