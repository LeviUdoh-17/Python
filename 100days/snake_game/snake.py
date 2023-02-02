from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move_up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)
    def move_down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)
    def move_left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)
    def move_right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def move(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            newx = self.segment[seg_num - 1].xcor()
            newy = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(newx, newy)
        self.head.fd(MOVE_DISTANCE)