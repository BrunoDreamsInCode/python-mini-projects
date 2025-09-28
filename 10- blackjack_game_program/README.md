# Blackjack Game

> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

- input() and user interaction
- Using lists to store cards
- Conditional statements (if/else) to check game outcomes
- while loops to control game flow
- Functions to organize code and reuse logic
- Random module to simulate drawing cards

## Description

This program simulates a simple Blackjack game between a player and the computer (dealer):

- Player and dealer are dealt cards
- Player can choose to draw more cards or pass
- Ace can count as 11 or 1 automatically to avoid bust
- Dealer draws cards automatically until reaching 17 or higher
- The program checks for Blackjack, busts, and declares a winner

### Example interaction:

Do you want to play a game of Blackjack? Type 'y' or 'n': y  

Your cards: [2, 10], current score: 12  
Computer's first card: 11  

Type 'y' to get another card, type 'n' to pass: y  

Your final hand: [2, 10, 3], final score: 15  
Computer's final hand: [11, 6], final score: 17  

💀 YOU LOSE!

Each run can have different cards and outcomes.

### Learning Goal

- Practice using lists to store and manipulate game data
- Learn to implement game logic with conditionals
- Understand loops for repeated player actions
- Learn to use functions for modular code
- Combine randomization, logic, and user input to build an interactive game

## How to Run
````
python blackjack_game.py
````