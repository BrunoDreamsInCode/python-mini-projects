from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        # Initialize score level
        self.level = 0
        self.penup()            # Prevent drawing lines while moving
        self.hideturtle()       # Hide the turtle shape (only text will be shown)
        self.color("white")     # Set text color
        self.goto(0, 280)       # Position the score text at the top of the screen
        self.display_text()     # Display the initial score

    def display_text(self):
        # Clear the previous score and display the updated value
        self.clear()
        self.write(f"Score: {self.level}", False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        # Display the final "Game Over" message in the center of the screen
        self.goto(0, 0)
        self.write(f"GAME OVER: {self.level}", False, align="center", font=("Arial", 15, "normal"))

    def level_up_score(self):
        # Increase the score by 1 and refresh the display
        self.level += 1
        self.display_text()