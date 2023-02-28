from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
image = "100days/day_25/us-states-game-start/blank_states_img.gif"
screen.title("U.S States Game")
screen.addshape(image)
Turtle().shape(image)

state_data = pd.read_csv("100days/day_25/us-states-game-start/50_states.csv")
correct_guesses = []
game_on = True
while game_on:
    if len(correct_guesses) == 50:
        game_on = False
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess The State", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        break
    for state in state_data["state"]:
        data_top = state_data[state_data["state"] == answer_state]
        if state == answer_state:
            taido = Turtle()
            taido.hideturtle()
            taido.pu()
            taido.goto(int(data_top.x), int(data_top.y))
            taido.write(answer_state)
            correct_guesses.append(answer_state)
skipped = []
for state in state_data["state"]:
    if state not in correct_guesses:
        skipped.append(state)
new_data = pd.DataFrame({"States": skipped})
new_data.to_csv("100days/day_25/us-states-game-start/states_to_learn.csv")
        