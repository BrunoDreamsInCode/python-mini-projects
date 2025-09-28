import random
import hangman_words
import hangman_art
lives = 6
print(hangman_art.logo)

# Select a random word from random_words list
chosen_word = random.choice(hangman_words.word_list)

# Initial placeholder
display = "_" * len(chosen_word)
print("Word to guess: " + display)

game_over = False
guessed_letters = []  # input all correct letters from player inpu

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue
    else:
        guessed_letters.append(guess)

    # Including a display
    new_display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            new_display += letter
        else:
            new_display += "_"

    print("Word to guess: " + new_display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    # Update display
    display = new_display

    # Check victory conditions
    if "_" not in display:
        game_over = True
        print(f"**************************** YOU WIN ****************************")
        print(f"IT WAS {chosen_word}!")
    elif lives == 0:
        game_over = True
        print(f"*********************** YOU LOSE **********************")
        print(f"IT WAS {chosen_word}!")
    print(hangman_art.stages[lives])


