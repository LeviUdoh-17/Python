from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=10, pady=10)

input = Entry(width=10)
input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.config(padx=10, pady=5)
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.config(padx=10, pady=5)
equal.grid(column=0, row=1)

mile_converted = 0
km_value = Label(text=f"{mile_converted}")
km_value.config(padx=10, pady=5)
km_value.grid(column=1, row=1)

km = Label(text="km")
km.config(padx=10, pady=5)
km.grid(column=2, row=1)

def button_clicked():
    mile_converted = int(input.get())*1.609
    km_value.config(text=f"{mile_converted}")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()