from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def calculate():
    miles = float(input.get())
    km = round(miles*1.609, 2)
    label2.config(text=km)


label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

label2 = Label(text="0")
label2.grid(column=1, row=1)

label3 = Label(text="Miles")
label3.grid(column=2, row=0)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

input = Entry(width=7)
input.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()