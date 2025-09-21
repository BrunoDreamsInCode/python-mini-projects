import random
from random import choice

# List of word options
word_list = ["aardvark", "baboon", "camel"]
placeholder = []
game_over = False

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Create a display
for letter in chosen_word:
    placeholder.append("_")

lives = 5
while not game_over:
    print(f"\nWord to guess: \n{' '.join(placeholder)}")

    print(f"\nRemaining lives: {lives}")
    chosen_letter = input("\nChoose a letter: ").lower()

    if chosen_letter in chosen_word:
        for index, letter in enumerate(chosen_word):
            if chosen_letter == letter:
                placeholder[index] = letter
        print("Letter found!")

    new_display = "".join(placeholder)

    if chosen_letter not in chosen_word:
        print("\nBad luck!")
        lives -= 1
        if lives <= 0:
            print("\nGame Over. You lost!")
            print(f"The word was: {''.join(chosen_word)}")
            game_over = True
        else:
            print("Keep trying\n")

    if new_display == chosen_word:
        print("\nYou WIN! You guessed it!")
        print(f"The word was: {''.join(new_display)}")
        game_over = True
