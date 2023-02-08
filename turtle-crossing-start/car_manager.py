from turtle import Turtle, Screen
from random import choice, randint


COLORS = []
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS = []

screen = Screen()
screen.colormode(255)
for _ in range(20):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        COLORS.append((r,g,b))
    
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.y_cor = randint(-250, 250)
        self.pu()
        self.normal_speed = STARTING_MOVE_DISTANCE
        self.speed_increase = MOVE_INCREMENT
        
    def create_car(self):
        self.shape("square")
        self.goto(300, self.y_cor)
        self.color(choice(COLORS))
        self.seth(180)
        self.turtlesize(stretch_len=2)
