MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# Current resources in the machine
resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
}

import time


# Clears the console
def clear():
    print("\n" * 50)

# Simple coffee animation
def coffee_animation():
    frames = [
        r"""
          ( (
           ) )
        ........
        |      |]
        \      /
         `----'
        """,
        r"""
           ) )
          ( (
        ........
        |      |]
        \      /
         `----'
        """,
    ]

    for i in range(10): # number of repetitions
        clear()
        print(frames[i % len(frames)])
        time.sleep(0.3)

    clear()
    print("Enjoy your drink")
    print(        r"""
                   ) )
                  ( (
                ........
  (ﾉ◕ヮ◕)ﾉ*:・ﾟ✧|       |]
                \      /
                 `----'
       
        """)

# Check if there are enough ingredients for the selected drink
def is_ingredients_enough(order_ingredients):
    for item, amount in order_ingredients.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Process the payment and return updated profit
def payment_check(drink_payment, profit):
    coin_quarter = float(input("How many quarter? :")) * 0.25
    coin_dimes = float(input("How many dimes? :")) * 0.10
    coin_nickles = float(input("How many nickles? :")) * 0.05
    coin_pennies = float(input("How many pennies? :")) * 0.01

    sum_coins = round(coin_quarter + coin_dimes + coin_nickles + coin_pennies, 2)
    drink_cost = MENU[drink_payment]['cost']
    change = sum_coins - drink_cost

    if sum_coins >= drink_cost:
        profit += change # Update profit with change
        stock_change(drink_payment) # Deduct ingredients
        coffee_animation()
    else:
        print("Sorry that's not enough money. Money refunded.")
    return profit

# Deduct used ingredients from resources
def stock_change(drink_stock):
    for i in MENU[drink_stock]['ingredients']:
        resources[i] -= MENU[drink_stock]['ingredients'][i]

# Deduct used ingredients from resources
def report():
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(profit,2)}\n")


machine_on = True
profit = 0 # initial profit

# Main loop
while machine_on:
    choice = ''
    valid_options = {'espresso', 'latte', 'cappuccino', 'report', 'off'}

    # Prompt user until a valid option is selected
    while True:
        choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
        if choice in valid_options:
            break
        print("Select a valid option")

    if choice == 'report':
        report()
    elif choice == 'off':
        print("(ㅠ﹏ㅠ)")
        print("Bye!")
        machine_on = False
    else:
        drink = MENU[choice]
        if is_ingredients_enough(drink["ingredients"]):
            profit = payment_check(choice, profit)  # update profit after payment
        else:
            print("\n(ㅠ﹏ㅠ)\n")
            print("Sorry, there is no resources available")


