from turtle import Screen
from paddle import Paddle
from ball import Ball, SPEED
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Pong")
scoreboard = Scoreboard()
ball = Ball()
paddle_r = Paddle([350, 0])
paddle_l = Paddle([-350, 0])
screen.listen()
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_r.move_down, "Down")
screen.onkeypress(paddle_l.move_down, "s")


game_on = True
while game_on:
    screen.update()
    scoreboard.refresh()
    time.sleep(SPEED)
    ball.ball_move()
    
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce()
    #to detect collision with the right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bat()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bat()

    if ball.xcor() >400:
        scoreboard.l_score += 1
        ball.reset_position()
        scoreboard.clear()
        scoreboard.refresh()

    if ball.xcor() < -400:
        # gameover = Scoreboard()
        # gameover.gameover()
        # game_on = False
        scoreboard.r_score += 1
        ball.reset_position()
        scoreboard.clear()
        scoreboard.refresh()



screen.exitonclick()