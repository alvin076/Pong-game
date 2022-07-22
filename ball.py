from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bound_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1
            self.move_speed *= 0.9

    def bound_x(self, p):
        if self.distance(p) < 50 and (self.xcor() > 320 or self.xcor() < -320):
            self.x_move *= -1
            self.move_speed *= 0.9

    def miss_ball(self, direction):
        if direction == 'r':
            if self.xcor() > 380:
                self.goto(0, 0)
                self.x_move *= -1
                self.move_speed = 0.1
                return True

        elif direction == 'l':
            if self.xcor() < -380:
                self.goto(0, 0)
                self.x_move *= -1
                self.y_move *= -1
                self.move_speed = 0.1
                return True

