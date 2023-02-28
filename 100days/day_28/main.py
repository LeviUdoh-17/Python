from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
mark = ""
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global mark, reps
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    mark = ""
    check_label.config(text=mark)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 > 0:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_sec)
    elif reps % 2 == 0 and reps % 8 != 0:
        title_label.config(text="Break", fg=RED)
        countdown(short_break_sec)
    else:
        title_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        global mark
        if reps == 0:
            mark = "✔"
            check_label.config(text=mark)
            
        if reps % 2 == 0:
            work_sessions = reps//2
            mark = "✔"*work_sessions
            check_label.config(text=mark)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#title
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

#canvas
canvas = Canvas(width=200, height=294, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="100days/day_28/tomato.png")
canvas.create_image(100, 122, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1 , row=1)


#buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0 , row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2 , row=2)

#checkmark
check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)


window.mainloop()