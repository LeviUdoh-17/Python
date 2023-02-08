from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0

    def refresh(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 68, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 68, "normal"))
    
    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 68, "normal"))