from turtle import Turtle
from urllib.response import addbase
from rfc3986.abnf_regexp import segments

# Direction constants (in degrees)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Movement constants
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        # List to hold all the turtle segments of the snake
        self.segments = []
        self.create_snake()  # Initialize the snake with its starting body
        self.head = self.segments[0]  # The first segment is considered the head
        self.last_tails = -40  # (Currently unused) could be for tracking the last tail position

    def create_snake(self):
        # Create the initial snake body using the starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Create a new turtle segment and add it to the snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # Prevent the segment from drawing lines
        new_segment.goto(position)
        self.segments.append(new_segment)

    def new_segment(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        # Move the snake forward by updating each segment's position
        # Each segment takes the position of the one in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head forward by a fixed distance
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change direction to UP only if not currently moving DOWN
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change direction to DOWN only if not currently moving UP
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # Change direction to RIGHT only if not currently moving LEFT
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # Change direction to LEFT only if not currently moving RIGHT
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)