from turtle import Turtle

X_COR = 350
Y_COR = 0

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.cor = pos
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(self.cor[0], self.cor[1])

    def move_up(self):
        self.cor[1] += 20
        self.goto(self.cor[0], self.cor[1])

    def move_down(self):
        self.cor[1] -= 20
        self.goto(self.cor[0], self.cor[1])