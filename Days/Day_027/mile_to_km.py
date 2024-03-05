from tkinter import *


def button_clicked():
    km = 1.60934
    new_text = float(input.get()) * km
    label_convert.config(text=new_text)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=30)

# Label Miles
label_mile = Label(text="Miles", font=("Arial", 20, "normal"))
label_mile.grid(column=2, row=0)

# Label equal
label_equal = Label(text="is equal to", font=("Arial", 20, "normal"))
label_equal.grid(column=0, row=1)

# Label convert
label_convert = Label(text="0", font=("Arial", 20, "normal"))
label_convert.grid(column=1, row=1)


# Label Km
label_km = Label(text="Km", font=("Arial", 20, "normal"))
label_km.grid(column=2, row=1)

# Button 01
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()
