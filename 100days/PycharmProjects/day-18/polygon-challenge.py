from turtle import Turtle, Screen
from random import randint
tim = Turtle()
screen = Screen()
angles = []
a = 0
screen.colormode(255)
for i in range(3, 11):
    angle = 360/i
    angles.append(angle)
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    for side in range(i):
        tim.pencolor(r, g, b)
        tim.fd(100)
        tim.right(angles[a])
    a += 1

screen.exitonclick()