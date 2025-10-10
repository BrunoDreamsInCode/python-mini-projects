import random
from turtle import Turtle, Screen

directions = [0,90,270]

colors = [
    "red", "green", "blue", "orange", "purple", "yellow",
    "pink", "cyan", "magenta", "lime", "gold", "brown",
    "violet", "turquoise", "indigo", "coral", "salmon",
    "khaki", "maroon", "navy", "teal", "olive", "gray",
    "black", "white"
]



def turtle_random(numbers_movement):
    bruno_the_turtle = Turtle()
    evolution_turtle = 0.1
    for i in range(numbers_movement):
        bruno_the_turtle.color(random.choice(colors))
        bruno_the_turtle.pencolor(random.choice(colors))

        turn_time = random.randint(0,1)
        if turn_time == 0:
            bruno_the_turtle.left(random.choice(directions))
        else:
            bruno_the_turtle.right(random.choice(directions))
        bruno_the_turtle.forward(20)
        bruno_the_turtle.pensize(1*evolution_turtle)
        bruno_the_turtle.speed(1+evolution_turtle)
        evolution_turtle = evolution_turtle + 0.1



turtle_random(400)



screen = Screen()
screen.exitonclick()