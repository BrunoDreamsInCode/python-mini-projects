import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Game setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Game objects
rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(rpaddle.move_up, "Up")
screen.onkey(rpaddle.move_down, "Down")
screen.onkey(lpaddle.move_up, "W")
screen.onkey(lpaddle.move_down, "S")

# Main game loop
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(rpaddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(lpaddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Right paddle miss
    if ball.xcor() > 380:
        scoreboard.l_side_point()
        ball.restart()

    # Left paddle miss
    if ball.xcor() < -380:
        scoreboard.r_side_point()
        ball.restart()

screen.exitonclick()
