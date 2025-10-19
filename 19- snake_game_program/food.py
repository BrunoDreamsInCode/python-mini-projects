import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Set the appearance of the food
        self.shape("circle")
        self.penup()                               # Prevent drawing when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make it smaller (half the default size)
        self.color("red")                          # Food color
        self.speed("fastest")                      # Move instantly when repositioning
        self.refresh()                             # Place the food at a random position initially

    def refresh(self):
        # Move the food to a random location within the screen boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)