from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make paddle taller
        self.goto(position)  # Set initial position

    def move_up(self):
        # Move paddle up by 20 units
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        # Move paddle down by 20 units
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
