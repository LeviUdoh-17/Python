#Used to extract the colors in hirst_image.jpg
# import colorgram

# color_set = colorgram.extract("day-18\hirst image.jpg", 6)
# colors = []
# for index in range(6):
#     color = color_set[index].rgb
#     r = color.r
#     g = color.g
#     b = color.b
#     color_rgb = (r, g, b)
#     colors.append(color_rgb)
# print(colors)
from random import choice, randint
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(255)
# color_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189)]
ypos = 35
ystart = -315
xstart = -400
xpos = 40
turtle.penup()
turtle.speed(0)
turtle.setpos(xstart, ystart)
for height in range(20):
    for step in range(20):
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        color = (r, g, b)
        turtle.fd(20); turtle.dot(20, color); turtle.fd(20)

    turtle.setpos(xstart, ystart+ypos*(height+1))
    

screen.exitonclick()