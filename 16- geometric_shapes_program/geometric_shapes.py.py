import random
from turtle import Turtle, Screen

# List of colors for the shapes
colors = ["red", "green", "blue", "orange", "purple", "yellow"]

def geometry_move(turtle):
    """
    Draws geometric shapes from triangle to nonagon with random colors.
    """
    num_sides = 3  # Start with a triangle
    for _ in range(7):  # Draw 7 shapes (triangle to nonagon)
        turn_angle = 360 / num_sides
        turtle.pencolor(random.choice(colors))  # Pick a random color for each shape
        for _ in range(num_sides):
            turtle.forward(100)
            turtle.left(turn_angle)
        num_sides += 1  # Increase the number of sides for the next shape

def main():
    # Create the turtle
    bruno_the_turtle = Turtle()
    bruno_the_turtle.shape("turtle")
    bruno_the_turtle.color("red")

    # Draw the shapes
    geometry_move(bruno_the_turtle)

    # Keep the screen open until clicked
    screen = Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()