import random
from turtle import Turtle, colormode

colormode(255)

INITIAL_POSITION = (250, -250)
ENEMY_SPEED = 5
ENEMY_INCREASE_SPEED = 10

# Generate a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

class EnemyManager:
    def __init__(self):
        self.all_enemies = []       # List to store all enemies
        self.enemy_speed = ENEMY_SPEED

    # Create a new enemy at random position
    def gen_enemy(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_enemy = Turtle("square")
            new_enemy.shapesize(stretch_wid=1, stretch_len=2)
            new_enemy.color(random_color())
            new_enemy.penup()
            random_y = random.randint(-250, 250)
            new_enemy.goto(300, random_y)
            self.all_enemies.append(new_enemy)

    # Move all enemies to the left
    def move_enemy(self):
        for enemy in self.all_enemies:
            enemy.backward(self.enemy_speed)

    # Increase enemy speed after each level
    def increase_enemy_speed(self):
        self.enemy_speed += ENEMY_INCREASE_SPEED