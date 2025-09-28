# HANGMAN GAME 

> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

- `input()` user interaction
- conditional statements
- loops (`while` and `for`)
- manipulation of (`strings` and `lists`)
- importing and organizing code into modules

## Versions

### Version 1: `v1_hangman_game_program.py`
A simple Hangman Game implementation:
- Randomly selects a word from a list (defined inside the code).
- Player can guess typing letters.
- Tracks remaining lives.
- Displays progress with underscores `_`.
- Ends the game with a Win or Lose message.

### Version 2: `v2_hangman_game_program.py`
An improved Hangman Game with extra features:
- Uses `hangman_words.py` to import the word list.
- Uses `hangman_art.py` to display logo and hangman stages.
- Shows the number of lives left each turn.
- Checks if the user already guessed a letter and avoids losing a life.
- Provides feedback when the guessed letter is not in the word.
- Reveals the correct word at the end of the game (Win or Lose).

---

## How to Play
1. Run the program (choose version 1 or 2).
   ```bash
    python v1_hangman_game_program.py
    python v2_hangman_game_program.py
    2. The game shows the word as underscores _ for each letter.
    3. Enter a letter when prompted.
    4. If the letter is in the word, it is revealed in the correct positions.
    5. If the letter is not in the word, you lose a life.
    6. The game ends when:
    7. You guess all letters correctly → You WIN!
    8. You run out of lives → Game Over!