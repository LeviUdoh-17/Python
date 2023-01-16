from random import choice, randint
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
turtle.penup()
turtle.speed("fastest")

turtle.setpos(-300, -290)
for height in range(60):
    for step in range(60):
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        color = (r, g, b)
        turtle.fd(5); turtle.dot(5, color); turtle.fd(5)
        print(turtle.position())
    turtle.setpos(-300, -290+10*(height+1))
    

screen.exitonclick()