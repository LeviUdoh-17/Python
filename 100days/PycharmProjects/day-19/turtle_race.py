from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
num = 0
y_axis = -75

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[num])
    tim.penup()
    tim.goto(x=-240, y=y_axis)
    all_turtles.append(tim)
    num += 1
    y_axis += 30
print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in all_turtles:
        current_position = turt.position()
        if 230 > current_position[0]:
            turt.fd(randint(0, 10))
        else:
            print(user_bet)
            winner = turt.color()
            if user_bet == winner[0]:
                print(f"Congratulations! You won, the {winner[0]} turtle is the winner")
            else:
                print(f"You lost! The winner is the {winner[0]} turtle")
            is_race_on = False
            

screen.exitonclick()