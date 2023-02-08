from turtle import Turtle


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.ht()
        self.pu()

    def level(self):
        self.goto(-260, 260)
        self.write(f"Level: {self.score}", align="left", font=("Courier", 16, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)