from tkinter import *
import pandas
from random import choice
import time

BACKGROUND_COLOR = "#B1DDC6"
timer = 0
known_dict = {}
count = 0
word_list = []
# ------------------------ READ FILE PANDA -------------------------- #
try :
    word_file = pandas.read_csv("100days/flash_card_project_Day_31/data/words_to_learn.csv")
except FileNotFoundError:
    word_file = pandas.read_csv("100days/flash_card_project_Day_31/data/french_words.csv")
    print(word_file)

word_list = word_file.to_dict(orient="records")
word_dict = {}

# ------------------------ RANDOM WORD SELECTION -------------------------- #

def already_know():
    global word_dict, known_dict
    known_dict[word_dict["French"]] = word_dict["English"]
    word_list.remove(word_dict)
    word_transition()
    data = pandas.DataFrame(word_list)
    data.to_csv("100days/flash_card_project_Day_31/data/words_to_learn.csv", index=False)

def to_learn():
    global word_dict
    french = word_dict["French"]
    english = word_dict["English"]
    # with open("100days/flash_card_project_Day_31/data/words_to_learn.csv", "a") as file:
    #     file.write(f"{french} : {english}\n")
    word_transition()

def word_transition():
    global word_dict, timer
    window.after_cancel(timer)
    word_dict = choice(word_list)
    canvas.itemconfig(language_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=word_dict['French'])
    canvas.itemconfig(background_image, image= front_page)
    flip_time()

def flip_page():
    global word_dict
    canvas.itemconfig(background_image, image= back_page)
    canvas.itemconfig(language_text, fill="white", text='English')
    canvas.itemconfig(word_text, fill="white", text=word_dict['English'])

def flip_time():
    global timer
    timer = window.after(5000, flip_page)

# ------------------------ FLASH CARD U.I -------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_page = PhotoImage(file="100days/flash_card_project_Day_31/images/card_front.png")
back_page = PhotoImage(file="100days/flash_card_project_Day_31/images/card_back.png")
background_image=canvas.create_image(400, 263, image=front_page)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="100days/flash_card_project_Day_31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=to_learn)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="100days/flash_card_project_Day_31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=already_know)
right_button.grid(row=1, column=1)

flip_time()
word_transition()

window.mainloop()