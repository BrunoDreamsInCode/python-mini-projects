from v3_menu import Menu
from v3_coffee_maker import CoffeeMaker
from v3_money_machine import MoneyMachine
from art import coffee


# Initialize the machine state (on/off)
machine_on = True

# Create objects for menu, coffee maker, and money machine
menu_drink = Menu()
stock = CoffeeMaker()
money = MoneyMachine()

# Main loop: keeps the coffee machine running
while machine_on:
    # Display available drink options
    options = menu_drink.get_items()
    choice = input(f"What would you like? {options}: ").lower()

    # Turn off the machine
    if choice == 'off':
        print("Bye!")
        machine_on = False

    # Print current resources and money report
    elif choice == 'report':
        stock.report()
        money.report()

    # Process drink order
    else:
        # Get the drink object that matches the user's choice
        selected_drink = menu_drink.find_drink(choice)

        # Check resources and payment before making the coffee
        if stock.is_resource_sufficient(selected_drink) and money.make_payment(selected_drink.cost):
            # Deduct ingredients and make the coffee
            stock.make_coffee(selected_drink)
            print(coffee)
