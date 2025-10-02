# Higher Lower Game

> Exercise from my current Python course. (https://www.udemy.com/course/100-days-of-code/)

Python exercise focused on learning:

- `input()` and user interaction  
- `for` loops and iteration  
- Working with lists and dictionaries  
- Random selection with `random.randint()`  
- Using functions to organize code  
- Conditional statements and logic for comparisons  
- Clearing the console with `os.system()`  

## Description

A game where the player guesses which account has more followers:

- Compare two accounts at a time (A vs B)  
- Each account includes **name**, **description**, **country**, and **follower count**  
- Program keeps track of the player's **score** for consecutive correct guesses  
- The next round always presents a new comparison, with B becoming A if guessed correctly  
- Visual ASCII art (`logo` and `vs`) enhances user experience  

### Example output:

Compare A: Instagram, a Social media platform, from United States.  
VS  
Against B: Cristiano Ronaldo, a Footballer, from Portugal.  

Who has more followers? Type 'A' or 'B': a  
🎉 You're right! 🎉 Current score: 1.  

Compare A: Instagram, a Social media platform, from United States.  
VS  
Against B: Dwayne Johnson, an Actor, from United States.  

Who has more followers? Type 'A' or 'B': b  
🎉 You're right! 🎉 Current score: 2.  

...  
Sorry, that's wrong. Final score: 3  

Each run generates a new sequence of comparisons, keeping the game unpredictable and challenging.

### Learning Goal

- Practice using randomization in Python  
- Work with lists and dictionaries to store and retrieve data  
- Combine loops, conditions, and functions to build a small interactive program  
- Improve console-based user interface skills  

## How to Run

```bash
python higher_lower.py
