from turtle import Turtle

#Initial constants
INITIAL_POSITION = (0,-280)
FINISH_LINE = (0,280)
PLAYER_MOVEMENT = 50


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(INITIAL_POSITION)

    #Move the player forward
    def move_up(self):
        self.forward(PLAYER_MOVEMENT)

    #Reset player to start position
    def reset_player(self):
        self.goto(INITIAL_POSITION)