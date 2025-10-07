Coffee Machine Simulator ☕

Exercise from 100 Days of Code Python Course
https://www.udemy.com/course/100-days-of-code/

A Python program that simulates a coffee vending machine with inventory management, payment processing, and user interaction.

Versions
--------
- v1_coffee_machine.py – Initial version: functional coffee machine with payment, inventory, and reporting.
- v2_coffee_machine.py – Updated version: added animation, modular functions, better input handling, and profit accumulation.

Features (v2)
--------------
- 3 Drink Options: Espresso ($1.50), Latte ($2.50), Cappuccino ($3.00)
- Inventory Tracking: Monitors water, milk, coffee, and money
- Coin Payment: Accepts quarters, dimes, nickles, pennies
- Auto Change: Calculates and returns exact change
- Stock Validation: Checks ingredients before processing orders
- Coffee Animation: ASCII animation when serving drinks
- Modular Functions: Payment, inventory, reporting, and animations separated for readability
- Improved Input Validation: Handles invalid input gracefully
- Profit Accumulation: Keeps track of earnings across multiple orders

Commands
--------
- espresso / latte / cappuccino – Order drinks
- report – Show resources and earnings
- off – Shutdown machine

How to Use
----------
1. Run the desired version:

python v1_coffee_machine.py
# or
python v2_coffee_machine.py

2. Select a drink:

What would you like? (espresso/latte/cappuccino): latte

3. Insert coins:

How many quarters? : 10
How many dimes? : 2
How many nickles? : 0
How many pennies? : 0

4. Receive drink and change:

Change: $0.0
Enjoy your latte! ☕

5. Check resources:

What would you like? (espresso/latte/cappuccino): report

Water: 900ml
Milk: 900ml
Coffee: 900g
Money: $2.5

Technical Skills
----------------
- Python dictionaries and data structures
- Modular function design and clean code
- User input validation and error handling
- Mathematical operations and state management
- Basic console animation with ASCII art

Requirements
------------
- Python 3.x
