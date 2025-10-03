from art import logo,vs
from game_data import data
import random


def clear_screen():
    print("\n" * 100)

# Take a user's data from game_data and return it formatted as a readable string
def format_data(user_data):
    user_name = user_data['name']
    user_desc = user_data['description']
    user_country = user_data['country']

    return f"{user_name} a {user_desc}, from {user_country}"

# Compare the follower counts of A and B and return True if the user's guess is correct
def compare_data(a_data, b_data, user_guess):
    followers_a = a_data['follower_count']
    followers_b = b_data['follower_count']

    if user_guess == 'a' and followers_a > followers_b:
        return True
    elif user_guess == 'b' and followers_b > followers_a:
        return True
    else:
        return False

# Main function that runs the Higher Lower game loop
def game():
    continue_game = True
    score = 0
    data_a = random.choice(data)
    print(logo)

    # If data A and data B are the same, pick a new B so the comparison is different
    while continue_game:
        data_b = random.choice(data)

        while data_a == data_b:
            data_b = random.choice(data)


        print(f"Compare A: {format_data(data_a)}")
        print(vs)
        print(f"Compare B: {format_data(data_b)}")

        guess = input ("Who has more followers? Type 'A' or 'B': ").lower()

        # Validate input to ensure the user types 'A' or 'B'
        while guess not in ['a', 'b']:
            guess = input("Please type 'A' or 'B': ").lower()

        clear_screen()
        print(logo)

        # Check if the user's guess is correct; if B was guessed correctly, set B as the next A
        if compare_data(data_a,data_b, guess):
            score += 1
            if guess == 'b':
                data_a = data_b
            print(f"😁You're right!😁 Current score: {score}📈.")
        else:
            print(f"😢Sorry😢, that's wrong. Final score: {score}📈.")
            continue_game = False


game()
# Loop to allow the player to play multiple times
# Validates input to accept only 'y' or 'n' and restarts the game if 'y' is chosen
want_play = True
while want_play:
    restart_game = input("\nDo you want play again ? 'y' or 'n': ").lower()
    while restart_game not in ['y', 'n']:
        restart_game = input("Do you want play again ? 'y' or 'n': ").lower()
    if restart_game == 'y':
        game()
    else:
        print("Bye!")
        want_play = False