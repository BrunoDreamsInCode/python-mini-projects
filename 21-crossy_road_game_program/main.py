import time
from turtle import Screen
from screenboard import Screenboard
from player import Player
from enemy import EnemyManager

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create game objects
player = Player()
enemy_manager = EnemyManager()
screenboard = Screenboard()

# Keyboard input
screen.listen()
screen.onkey(fun=player.move_up, key="Up")

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    enemy_manager.gen_enemy()
    enemy_manager.move_enemy()

    # Check if player reached the top
    if player.ycor() > 280:
        player.reset_player()
        screenboard.level_up()
        enemy_manager.increase_enemy_speed()

    # Detect collision between player and enemies
    for enemy in enemy_manager.all_enemies:
        if enemy.distance(player) < 20:
            screenboard.game_over()
            game_on = False

# Keep screen open until user clicks
screen.exitonclick()