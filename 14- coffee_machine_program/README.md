# Coffee Machine Simulator

> Exercise from [100 Days of Code Python Course](https://www.udemy.com/course/100-days-of-code/)

A Python program that simulates a coffee vending machine with complete inventory management, payment processing, and user interaction.

## Description

A fully functional coffee machine simulator that allows users to purchase beverages, processes payments with coins, manages ingredient inventory, and provides real-time reporting.

# Coffee Machine Simulator ☕

A Python program that simulates a coffee vending machine with inventory management and payment processing.

## Features

- **3 Drink Options**: Espresso ($1.50), Latte ($2.50), Cappuccino ($3.00)
- **Inventory Tracking**: Monitors water, milk, coffee, and money
- **Coin Payment**: Accepts quarters, dimes, nickles, pennies
- **Auto Change**: Calculates and returns exact change
- **Stock Validation**: Checks ingredients before processing orders

## Commands

- `espresso` / `latte` / `cappuccino` - Order drinks
- `report` - Show resources and earnings
- `off` - Shutdown machine

## How to Use

1. Run the program:
```bash
python v1_coffee_machine.py
```

2. Order a drink:
What would you like? (espresso/latte/cappuccino): latte

3. Insert coins:
How many quarters? : 10
How many dimes? : 2
How many nickles? : 0  
How many pennies? : 0

4. Receive drink and change:
Change: $0.0
Here is your latte!

## Example Output
What would you like? (espresso/latte/cappuccino): report

Water: 900ml
Milk: 900ml  
Coffee: 900g
Money: $2.5

## Technical Skills

- Python dictionaries and data structures
- Function organization and modular code
- User input validation and error handling
- Mathematical operations and state management

## Requirements

- Python 3.x
- `art` module (optional, for coffee ASCII art)


