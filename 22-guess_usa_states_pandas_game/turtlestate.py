from turtle import Turtle

class TurtleState(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor
        self.penup()       # Prevent drawing lines when moving

    def goto_state(self, state, x_cor, y_cor):
        self.goto(x_cor, y_cor)  # Move turtle to the state's coordinates
        self.write(state)        # Display the state name at the coordinates
