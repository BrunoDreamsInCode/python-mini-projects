========================================
BLACKJACK GAME – VERSIONS 1 & 2
========================================

This repository contains two versions of a simple Blackjack game
developed in Python as part of my learning journey.

Both versions were implemented independently, and the second
version is an improved and optimized rewrite based on reflection
and understanding of the rules and logic.

----------------------------------------
VERSION 1
----------------------------------------

- First implementation of the Blackjack game
- Focused on basic game logic and player interaction
- Player and dealer receive cards
- Player can choose to draw more cards or pass
- Aces automatically adjusted to prevent bust
- Dealer draws automatically until reaching 17
- Includes messages and emojis for user experience

Learning Goals Achieved:
- Using lists to store and manipulate game data
- Conditional statements for game outcomes
- Loops to control repeated actions
- Functions for modular code
- Randomization and input handling

----------------------------------------
VERSION 2
----------------------------------------

- Fully rewritten and optimized version after reflecting on 
  the instructor's solution
- Improved readability and user experience
- Calculates scores more efficiently and handles multiple Aces
- Natural Blackjack now clearly displayed as 21 instead of 0
- Player and dealer turns flow more logically
- Final results clearly displayed with fun messages
- Better modularity and code structure

Learning Goals Achieved:
- Enhanced modular code with functions
- Accurate implementation of Blackjack rules
- Edge case handling (Blackjack, multiple Aces, busts)
- Clearer and more user-friendly display
- Demonstrates independent problem-solving and code improvement

----------------------------------------
EXAMPLE INTERACTION (V2)
----------------------------------------

Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [11, 10], current score: 21
Computer's first card: 9

Your final hand: [11, 10], final score: 21
Computer's final hand: [9, 8, 10], final score: 27

😎 Win with a Blackjack!

----------------------------------------
HOW TO RUN
----------------------------------------
````bash
Run V1:
python v1_blackjack_game.py

Run V2:
python v2_blackjack_game.py
```` 
----------------------------------------
DIFFERENCES & IMPROVEMENTS (V2 vs V1)
----------------------------------------

- Cleaner and more readable code
- Better handling of multiple Aces
- Shows natural Blackjack as 21 instead of 0
- Improved messages and final output
- Optimized loops and function usage
- Clear separation of player and dealer turns
- More structured and modular for portfolio presentation

========================================