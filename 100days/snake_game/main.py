from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
score_count = 0

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    score = Scoreboard(score_count)
    score.ht()
    score.give_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    score.refresh()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_count += 1


    #Detect collision with the wall
    game_over = Scoreboard(score_count)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        game_over.goto(0,0)
        score.give_score()
        game_over.gameover()
    
    #Detect collision with tail
    for segment in snake.segment[1:len(snake.segment)]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            game_over.gameover()

screen.exitonclick()