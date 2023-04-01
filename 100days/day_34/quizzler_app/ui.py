from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.title_label = Label(text=f"score:{0}")
        self.title_label.config(padx=20, fg="white", background=THEME_COLOR)
        self.title_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.questions = self.canvas.create_text(150, 125, width=280,  text=f"Questions", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.true_image = PhotoImage(file="100days/day_34/quizzler_app/images/true.png")
        self.false_image = PhotoImage(file="100days/day_34/quizzler_app/images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0,padx=20, pady=20, command= self.true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=self.false_image, highlightthickness=0,padx=20, pady=20, command= self.false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions, text=q_text)
        else:
            self.canvas.itemconfig(self.questions, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self) :
        score = self.quiz.check_answer("True")
        self.title_label.config(text=f"Score: {score[0]}")
        self.give_feedback(score[1])

    def false(self) :
        score = self.quiz.check_answer("False")
        self.title_label.config(text=f"Score: {score[0]}")
        self.give_feedback(score[1])

    def give_feedback(self, is_true):
        if is_true == True:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
        
        
