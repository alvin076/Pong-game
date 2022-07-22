from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

screen.listen()
screen.onkey(r_paddle.moving_up, 'Up')
screen.onkey(r_paddle.moving_down, 'Down')
screen.onkey(l_paddle.moving_up, 'w')
screen.onkey(l_paddle.moving_down, 's')

ball = Ball()
scoreboard = ScoreBoard()
screen.update()

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.bound_y()
    ball.bound_x(l_paddle)
    ball.bound_x(r_paddle)

    if ball.miss_ball('r'):
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

    if ball.miss_ball('l'):
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()

