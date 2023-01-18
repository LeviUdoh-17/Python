from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.fd(10)

def backward():
    tim.bk(10)

def counterClockwise():
    tim.lt(10)

def clockwise():
    tim.rt(10)

def reset():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counterClockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(reset, "c")

screen.exitonclick()