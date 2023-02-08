from turtle import Turtle

SPEED = 0.1
POSITION = [0, 0]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        
    def ball_move(self):
        if self.ycor() < 321:
            self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
            # self.seth(78)
            # print(self.ycor())
            # self.fd(10)
        # else:
        #     self.seth(360-self.heading())
        #     self.fd(10)

    def bounce(self):
        self.y_move *= -1

    def bat(self):
        self.x_move *= -1
        global SPEED
        SPEED *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        global SPEED
        SPEED = 0.1
        self.bat()