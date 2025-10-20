from time import sleep
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # Update ball position
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse vertical direction
        self.y_move *= -1

    def bounce_x(self):
        # Reverse horizontal direction and slightly increase speed
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        # Reset position and speed after a point is scored
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()