import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Score

# Set up the game window
screen = Screen()
screen.tracer(0)  # Turn off automatic screen updates for smoother animation
screen.setup(width=600, height=640)
screen.bgcolor("black")

# Create the main game objects
snake = Snake()
food = Food()
score = Score()

# Listen for key inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_on = True
while game_on:
    screen.update()       # Refresh the screen manually
    time.sleep(0.1)       # Control the speed of the game

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.level_up_score()
        snake.new_segment()  # Add a new segment to the snake
        food.refresh()       # Move the food to a new random location

    # Detect collision with walls
    if (
        snake.head.xcor() < -280 or
            snake.head.xcor() > 280 or
            snake.head.ycor() > 280 or
        snake.head.ycor() < -280
    ):
        game_on = False
        score.game_over()

    # Detect collision with tail
    # If the head collides with any part of the tail, game over
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            score.game_over()

    # Move the snake forward
    snake.snake_move()

# Exit on click
screen.exitonclick()
