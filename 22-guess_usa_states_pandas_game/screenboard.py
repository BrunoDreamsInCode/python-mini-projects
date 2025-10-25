from turtle import Turtle

TOTAL_STATES = 50  # Total number of states in the game

class ScreenBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()      # Hide the turtle cursor
        self.penup()           # Prevent drawing lines when moving
        self.goto(-360, 260)   # Position for displaying score
        self.level = 0         # Initialize score counter

    def screen_score(self):
        self.clear()  # Clear previous score
        # Display current number of correctly guessed states
        self.write(f"States {self.level}/{TOTAL_STATES}", font=("Arial", 16, "bold"))

    def level_up(self):
        self.level += 1          # Increase score when a correct guess is made
        self.screen_score()      # Update score display
        if self.level >= 50:     # Check if all states are guessed
            self.clear()         # Clear the screen
            self.you_win()       # Display winning message

    def you_win(self):
        # Display final score and congratulations message
        self.write(f"States {self.level}/{TOTAL_STATES}\nCongratulations!!!", font=("Arial", 16, "bold"))
