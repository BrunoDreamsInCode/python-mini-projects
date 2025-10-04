MENU = {
    "espresso": {
        "ingredients": {
            "water": 40,
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

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money": 0,  # Added money to track earnings
}

from art import coffee


def report_resources(actual_stock):
    """Generate a report of current resources"""
    return f"\nWater: {actual_stock['water']}ml\nMilk: {actual_stock['milk']}ml\nCoffee: {actual_stock['coffee']}g\nMoney: ${actual_stock['money']}\n"


def check_if_ingredients_available(menu_options, selection_drink, resources_stock):
    """Check if there are enough ingredients to make the selected drink"""
    ingredients_needed = menu_options[selection_drink]['ingredients']

    # Check each ingredient required for the drink
    for ingredient, amount in ingredients_needed.items():
        if resources_stock[ingredient] < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True


def deduct_from_stock(menu_options, resource_stock, drink):
    """Deduct the required ingredients from stock after making a drink"""
    for ingredient, amount in menu_options[drink]['ingredients'].items():
        resource_stock[ingredient] -= amount


def add_money(resource_stock, amount):
    """Add money to the machine's earnings"""
    resource_stock['money'] += amount


def check_money_amount(drink_check_cost, menu_cost_options, actual_resources):
    """Process payment and handle coin transactions"""
    # Get coin inputs from user
    coin_quarters = int(input("How many quarters? : "))
    coin_dimes = int(input("How many dimes? : "))
    coin_nickles = int(input("How many nickles? : "))
    coin_pennies = int(input("How many pennies? : "))

    # Calculate total amount inserted
    total_amount = (coin_quarters * 0.25) + (coin_dimes * 0.10) + (coin_nickles * 0.05) + (coin_pennies * 0.01)
    drink_cost = menu_cost_options[drink_check_cost]['cost']

    # Check if enough money was inserted
    if total_amount >= drink_cost:
        change = total_amount - drink_cost
        change = round(change, 2)
        print(f"\nChange: ${change}")

        # Process successful transaction
        deduct_from_stock(menu_cost_options, actual_resources, drink_check_cost)
        add_money(actual_resources, drink_cost)

        print("Here is your drink\n")
        print(coffee)
        return True
    else:
        # Handle insufficient funds
        print(f"\nYou selected a ${drink_cost} drink, your total is ${round(total_amount, 2)}")
        print(f"You need ${round(drink_cost - total_amount, 2)} more.")

        # Ask if user wants to insert more coins
        more_coin_or_cancel = input("Insert more coins? 'y' or 'n': ").lower()
        if more_coin_or_cancel == 'y':
            while total_amount < drink_cost:
                print("\nPlease insert more coins:")
                new_coin_quarters = int(input("How many quarters? : "))
                new_coin_dimes = int(input("How many dimes? : "))
                new_coin_nickles = int(input("How many nickles? : "))
                new_coin_pennies = int(input("How many pennies? : "))

                # Calculate additional coins
                new_total_amount = ((new_coin_quarters * 0.25) + (new_coin_dimes * 0.10) +
                                    (new_coin_nickles * 0.05) + (new_coin_pennies * 0.01))
                total_amount += new_total_amount

                print(f"\nYour money: ${round(total_amount, 2)}\nDrink cost: ${round(drink_cost, 2)}")

                # Check if enough after additional coins
                if total_amount >= drink_cost:
                    change = total_amount - drink_cost
                    change = round(change, 2)
                    print(f"\nChange: ${change}")

                    # Process successful transaction
                    deduct_from_stock(menu_cost_options, actual_resources, drink_check_cost)
                    add_money(actual_resources, drink_cost)

                    print("Here is your drink\n")
                    print(coffee)
                    return True
        else:
            # Refund money if user cancels
            print(f"Here is your money back: ${round(total_amount, 2)}")
            return False


def coffee_machine():
    """Main function to run the coffee machine"""
    machine_on = True

    while machine_on:
        # Get user selection
        user_selection = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if user_selection == 'off':
            # Turn off the machine
            machine_on = False
            print("Turning off coffee machine...")

        elif user_selection == 'report':
            # Display current resources
            print(report_resources(resources))

        elif user_selection in ['espresso', 'latte', 'cappuccino']:
            # Process drink order
            if check_if_ingredients_available(MENU, user_selection, resources):
                check_money_amount(user_selection, MENU, resources)
            else:
                print("Sorry, this item is not available.")

        else:
            # Handle invalid input
            print("Invalid option. Please choose: espresso, latte, cappuccino, report, or off.")


# Start the coffee machine
coffee_machine()