from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
#increase the pen size
tim.pensize(10)
screen.colormode(255)
#increase the turtle's speed
tim.speed(0)
#create the random walk
angles = [0, 90, 180, 360]


for i in range(200):
    angle = randint(0, 3)
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    
    tim.pencolor(r, g, b)
    #tim moves 25paces forward
    tim.fd(25)
    #tim moves at a random angle between 0, 90, 180, 360
    tim.setheading(angles[angle])