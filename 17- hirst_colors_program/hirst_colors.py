import random
import colorgram
from turtle import Turtle, Screen, colormode

# Set the color mode to 255 (RGB)
colormode(255)

# Extract 10 colors from the image
colors = colorgram.extract('hirst.jpg', 10)
colors_list = []

# Convert the colors to RGB tuples and store them in a list
for color in range(len(colors)):
    rgb = colors[color].rgb
    colors_list.append((rgb.r, rgb.g, rgb.b))

# Create the turtle
bruno_tataruga = Turtle()
screen = Screen()
bruno_tataruga.shape("turtle")

# Set the background color of the screen
screen.bgcolor("#828282")

# Set pen thickness and turtle speed
bruno_tataruga.pensize(15)
bruno_tataruga.speed("fastest")  # fastest speed
bruno_tataruga.hideturtle()  # hide the turtle icon
bruno_tataruga.penup()

# Starting coordinates
x1 = -400
y1 = -350

# Draw a 10x10 grid
for y in range(10):
    bruno_tataruga.setpos(x1, y1)  # move to the beginning of the row
    for x in range(10):
        # Pick a random color from the extracted colors
        bruno_tataruga.dot(20, random.choice(colors_list))  # draw a tiny line
        bruno_tataruga.forward(50) # move to the next column
    y1 += 50      # move down to the next row

# Keep the window open until clicked
screen.exitonclick()