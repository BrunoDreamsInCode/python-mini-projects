# Coffee Machine Simulator ☕

Exercise from 100 Days of Code Python Course  
https://www.udemy.com/course/100-days-of-code/

A Python program simulating a coffee vending machine with inventory, payments, and user interaction. Version 3 uses Object-Oriented Programming.

## Versions
- **v1** – Functional machine with payments, inventory, and reporting.
- **v2** – Added ASCII animation, modular functions, input validation, and profit tracking.
- **v3** – Refactored with classes (Menu, CoffeeMaker, MoneyMachine); modular, maintainable, OOP.

## Features (v3)
- 3 Drinks: Espresso (`$1.50`), Latte (`$2.50`), Cappuccino (`$3.00`)
- Tracks water, milk, coffee, and money
- Accepts coins and returns change
- Checks ingredients before making coffee
- Coffee animation (ASCII)
- Object-Oriented Design: modular classes and methods
- Profit tracking
- Improved input validation

## Commands
- `espresso` / `latte` / `cappuccino` – Order drinks
- `report` – Show resources and earnings
- `off` – Shutdown machine

## How to Use
1. Run the desired version:

   - For version 1:
     ```
     python v1_coffee_machine.py
     ```

   - For version 2:
     ```
     python v2_coffee_machine.py
     ```

   - For version 3:
     ```
     python v3_coffee_machine.py
     ```


2. Select drink and insert coins
3. Receive drink and change
4. Use `report` to check resources and money

## Technical Skills
- Object-Oriented Programming
- Modular code design
- Input validation and error handling
- State management and calculations
- ASCII animation

## Requirements
- Python 3.x