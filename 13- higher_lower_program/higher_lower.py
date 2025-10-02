from art import logo, vs
from random import randint
from game_data import data
import os

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to generate a "B" option that is different from the current "A"
def data_generate(index_a):
    index_b = index_a
    while index_b == index_a:  # Keep generating until we get a different index
        index_b = randint(0, len(data)-1)
    return data[index_b], index_b  # Return the B data and its index

def game():
    score = 0
    game_over = False

    # Choose the first random option for "A"
    index_a = randint(0, len(data)-1)
    data_a = data[index_a]

    while not game_over:
        clear_screen()  # Clear the screen for a fresh round
        print(logo)

        # Display current score if the player has points
        if score > 0:
            print(f"🎉 You're right! 🎉 Current score: {score}.\n")

        # Extract data for "A"
        name_a = data_a['name']
        description_a = data_a['description']
        country_a = data_a['country']
        followers_a = data_a['follower_count']
        print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")

        print(vs)  # Print the versus art

        # Generate the "B" option ensuring it is different from "A"
        data_b, index_b = data_generate(index_a)
        name_b = data_b['name']
        description_b = data_b['description']
        country_b = data_b['country']
        followers_b = data_b['follower_count']
        print(f"Against B: {name_b}, a {description_b}, from {country_b}.\n")

        # Ask the user who has more followers and validate input
        who_wins = input("Who has more followers? Type 'A' or 'B': ").lower()
        while who_wins not in ['a', 'b']:
            who_wins = input("Please type 'A' or 'B': ").lower()

        # Check if the user's guess is correct
        if (who_wins == 'a' and followers_a > followers_b) or (who_wins == 'b' and followers_b > followers_a):
            score += 1  # Increment score if correct
            # If player chose B and is correct, update "A" to the previous "B"
            if who_wins == 'b':
                data_a = data_b
                index_a = index_b
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True  # End the game if guess is wrong

# Loop to allow the player to play again
play_again = True
while play_again:
    game()  # Start a new game
    continue_playing = input("\nDo you want to play again? 'y' or 'n': ").lower()
    play_again = continue_playing == 'y'
    if not play_again:
        print("\nBye!")  # Exit message