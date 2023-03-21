from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json

# ---------------------------- SEARCH SETUP -------------------------------- #

def search():
    website = (website_input.get())
    try:
        with open("100days/day_29/data.json", "r") as file:
            data_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Datatype not found")
    else:
        if website in data_dict:
            password = data_dict[f"{website}"]["password"]
            usename = data_dict[f"{website}"]["email"]
            messagebox.showinfo(title=website, message=f"Email: {usename} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_passwords():
    global password_input
    password = generate_password()
    pyperclip.copy(password)
    password_input.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_info():
    global website_input, username_input, password_input
    new_data = {
        website_input.get(): {
            "email": username_input.get(),
            "password": password_input.get()
        }
    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: \nEmail: {username_input.get()} \nPassword: {password_input.get()} \nIs it okay to save?")
        if is_ok:
            try:
                with open("100days/day_29/data.json", "r") as file:
                    # file.write(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
                    # json.dump(new_data, file, indent=4)
                    data = json.load(file)
            except FileNotFoundError:
                with open("100days/day_29/data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:       
                data.update(new_data)
                with open("100days/day_29/data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)     
                password_input.delete(0, END)   

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file="100days/day_29/logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

#website
website_label = Label(text="Website:", pady=3)
website_label.grid(row=1, column=0)

website_input = Entry(width=32)
website_input.focus()
website_input.grid(row=1, column=1)

search = Button(text="Search", command=search, padx=0, pady=0, width=14)
search.grid(row=1, column=2)

#Email/Username
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=50)
username_input.insert(END, "ukaraobong15@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)

#Password
password_label = Label(text="Password:", pady=3)
password_label.grid(row=3, column=0)

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_passwords, padx=0, pady=0, width=14)
generate_button.config(justify="left")
generate_button.grid(row=3, column=2)

#Add
add_button = Button(text="Add", command=add_info)
add_button.config(width=43, padx=0, justify="center")
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()