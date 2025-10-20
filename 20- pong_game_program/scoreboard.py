from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0  # Left player score
        self.r_score = 0  # Right player score
        self.update_scoreboard()

    def update_scoreboard(self):
        # Display the scores on the screen
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Ariel", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Ariel", 60, "normal"))

    def l_side_point(self):
        # Increment left player score and update display
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_side_point(self):
        # Increment right player score and update display
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
