from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

LILAC = "#d68dfc"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    generated_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def buttonadd():
    website = input_site.get()
    username = input_id.get()
    password = generated_password.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_30/Password/data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_30/Password/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:  
            #updating old data with new data
            data.update(new_data)
                
            with open("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_30/Password/data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:        
                input_site.delete(0, END)
                generated_password.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_site.get()
    try:
        with open("N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_30/Password/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=LILAC)

# label padlock
canvas = Canvas(height=200, width=200, bg=LILAC, highlightthickness=0)
padlock_img = PhotoImage(
    file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_30/Password/logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0, padx=(0, 100))

# ********LABELS********
# Label website
web_label = Label(text="Website:", bg=LILAC)
web_label.grid(column=0, row=1, padx=(10, 0))

# Label Email/Username
id_label = Label(text="Email/Username:", bg=LILAC)
id_label.grid(column=0, row=2, padx=(10, 0))

# Label Password
pass_label = Label(text="Password:", bg=LILAC)
pass_label.grid(column=0, row=3, padx=(10, 0))

# ********ENTRYS********
# Entry website
input_site = Entry(width=20)
input_site.grid(column=1, row=1, padx=(0, 250))
input_site.focus()

# Entry email/username
input_id = Entry(width=45)
input_id.grid(column=1, row=2, columnspan=2, padx=(0, 100))
input_id.insert(0, "fernandofabner@gmail.com")

# Entry blank
generated_password = Entry(width=20)
generated_password.grid(column=1, row=3, padx=(0, 250))

# ********BUTTONS********
# Button Generate
button_generate_password = Button(
    width=18, text="Generate Password", command=generate)
button_generate_password.grid(column=1, row=3, padx=(20, 0))
# Button ADD
button_add = Button(width=36, text="Add", command=buttonadd)
button_add.grid(column=0, row=4, columnspan=3)
# Button Search
search_button = Button(text="Search", width=18, command=find_password)
search_button.grid(row=1, column=1, padx=(20, 0))

window.mainloop()
