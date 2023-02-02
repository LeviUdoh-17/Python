from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.color("white")
        self.penup()
        self.goto(0, 280)
    
    def give_score(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def gameover(self):
        self.write(f"GAME OVER", align= ALIGNMENT, font= FONT)

    def refresh(self):
        self.clear()