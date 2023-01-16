from turtle import Turtle, Screen
from random import randint
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
angle = 0
def spirograph(space):
    for _ in range(int(360/space)):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        tim.pencolor(r, g, b)
        for _ in range(1):
            global angle
            tim.setheading(angle)
            tim.circle(100)
        angle += space
spirograph(10)
screen.exitonclick()