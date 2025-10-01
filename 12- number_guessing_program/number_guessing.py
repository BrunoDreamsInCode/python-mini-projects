import os
from art import logo
import random
not_game_over = True

def check_number(number,random_number_func):
    if number == random_number_func:
        return 0 # Return 0 if the player guessed the right number
    elif number > random_number_func: #return 0 if the player got the number
        return 1 # Return 1 if the player guessed a higher number
    elif number < random_number_func:
        return 2 # Return 2 if the player guesses a lower number

while not_game_over:
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print("🤔 I'm thinking of a number between 1 and 100 🤔\n")

    # Create the target random number
    random_number = random.randint(1,100)


    difficulty = input("Choose a difficulty. Type 😃'easy' or 'hard'😱 : ").lower()

    # Set number of attempts based on chosen difficulty
    if difficulty == 'easy':
        life = 10
    elif difficulty == 'hard':
        life = 5
    else:
        print("Invalid Option")
        not_game_over = True
        break


    while life > 0:
        print(f"You have {life} attempts remaining to guess the number.")
        num = int(input ("Make a guess: "))

        # Validation of the guess: too low, too high, or correct
        state_check = check_number(num, random_number)

        if state_check == 0:
            print(f"\n🎉🥳🎉🥳You got it! The answer was {num}🎉🥳🎉🥳\n")
            life = -1
        elif state_check == 1:
            print("Too high 👀")
            life -= 1
        else:
            print("Too low 🤏")
            life -= 1
    else:
        if life == 0:
            print("You've run out of guesses. Refresh the page to run again.")

    play_again = input("Restart game ? type 'yes' or 'no': ").lower()
    if play_again != 'yes':
        not_game_over = False