from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#How to create a label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#changing arguements
my_label["text"] = "New Text initial"
my_label.config(text="New text final", padx=20, pady=20)
my_label.grid(column=0, row=0)


#Buttons
def button_clicked():
    my_label.config(text=input.get())
    

button = Button(text="Click Me", command=button_clicked)
button.config(padx=20, pady=20)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.config(padx=20, pady=20)
new_button.grid(column=2, row=0)

#Entry Component
input = Entry(width=10)
# input.config(padx=20, pady=20)
input.grid(column=3, row=3)

window.mainloop()