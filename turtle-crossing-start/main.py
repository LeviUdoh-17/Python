import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, STARTING_MOVE_DISTANCE, CARS
from scoreboard import Scoreboard
from random import randint, choice

screen = Screen()
screen.setup(width=600, height=650)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")


count = 0
sleep_time = 0.1
score = 1

level = Scoreboard(score)

game_is_on = True
while game_is_on:
    level.level()
    time.sleep(sleep_time)
    if count % 6 == 0:
        car = CarManager()
        car.create_car()
        CARS.append(car)
    for car in CARS:
        car.fd(car.normal_speed)
        if player.distance(car) <= 30:
            game_is_on = False
            game_over = Scoreboard(score)
            game_over.gameover()
    if player.ycor() == FINISH_LINE_Y:
        player.reposition()
        sleep_time *= 0.9
        level.clear()
        level.score += 1
    
    screen.update()
    count += 1
screen.exitonclick()