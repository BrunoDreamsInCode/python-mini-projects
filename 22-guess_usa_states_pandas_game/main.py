from turtle import Turtle, Screen
from turtlestate import TurtleState
import pandas
from screenboard import ScreenBoard

# Import data from CSV
data_state = pandas.read_csv("50_states.csv")

# List with all states for validation
state_validation = data_state["state"].to_list()

# Screen object for score and guesses
screenboard = ScreenBoard()

# Screen object
screen = Screen()
screen.addshape("blank_states_img.gif")
# screen.setup(height=491, width=725)  # Optional: setup window size

# Turtle object for showing state names
turtle_state = TurtleState()

# Background map
turtle = Turtle()
turtle.shape("blank_states_img.gif")
turtle.penup()  # Prevent drawing lines while moving

# Display initial score
screenboard.screen_score()

# Lists to track guessed states and states to learn
guessed_states = []
states_to_learn = []

# Game loop
game_on = True
while game_on:
    # Ask user for a guess
    guess = screen.textinput("Guess the State", "Your guess: ", ).title()

    # Exit condition
    if guess == "Exit":
        print(guessed_states)
        break

    # Check if guess is correct
    if guess in state_validation:
        # Only count if not guessed already
        if guess not in guessed_states:
            guessed_states.append(guess)  # Save correct guess

            # Find coordinates for the state
            find_line = data_state["state"] == guess
            x_cor = data_state[find_line].x.values[0]
            y_cor = data_state[find_line].y.values[0]

            # Move turtle to state coordinates and display name
            turtle_state.goto_state(guess, x_cor, y_cor)

            # Update score
            screenboard.level_up()
    else:
        pass  # Ignore wrong guesses

# After game ends, save states not guessed for learning
for state in state_validation:
    if state not in guessed_states:
        states_to_learn.append(state)

# Export states to learn to CSV
csv_learn_states = pandas.DataFrame(states_to_learn, columns=["States"])
csv_learn_states.to_csv("States_to_learn.csv", index=False)
