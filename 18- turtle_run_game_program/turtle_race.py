from turtle import Turtle, Screen
import random

# Create turtles that will race
faide = Turtle(shape="turtle")
lamic = Turtle(shape="turtle")
exctasy = Turtle(shape="turtle")
pokiz = Turtle(shape="turtle")
imp_hall = Turtle(shape="turtle")
shiv = Turtle(shape="turtle")

turtles = [faide, lamic, exctasy, pokiz, imp_hall, shiv]

# Track each turtle's progress in the race
finish_line = [0] * len(turtles)

# Set up the screen for the race
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to bet on a turtle color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ").lower()

# Assign a unique color to each turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial vertical position for placing turtles
y = -150

# X coordinate of the finish line
finish = 200

# Function to draw the finish line
def line_turtle(finish):
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(finish, -170)  # Start drawing the line from bottom
    line.left(90)
    line.pendown()
    line.forward(190)        # Draw vertical finish line

line_turtle(finish)

# Position all turtles at the starting line
for i, turtle in enumerate(turtles):
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-190, y)
    y += 30  # Space turtles evenly vertically

# Main loop to run the race
run = True
while run:
    for i, turtle in enumerate(turtles):
        random_move = random.randint(1, 4)  # Random step for each turtle
        turtle.forward(random_move)
        finish_line[i] += random_move       # Update distance moved
        if turtle.xcor() >= finish:         # Check if turtle reached finish
            color_winner = turtle.color()[0]
            if user_bet == color_winner:
                print(f"You win, the turtle {color_winner} WON!")
            else:
                print(f"You lose, the turtle {color_winner} WON!")
            run = False
            break

# Wait for user click to close the window
screen.exitonclick()