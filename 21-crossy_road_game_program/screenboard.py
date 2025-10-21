import turtle
from turtle import Turtle

#Constant font
FONT = ("Courier", 16, "bold")

class Screenboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230,270)
        self.level = 1
        self.show_level()

    #Displays current level
    def show_level(self):
        self.clear()
        self.write(f"Level = {self.level}", align="center", font=FONT)

    #Increase level by 1
    def level_up(self):
        self.level += 1
        self.show_level()

    #Show "Game Over" message
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
