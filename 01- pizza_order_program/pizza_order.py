print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ").lower()
if size == 's':
    final_bill = 15
elif size == 'm':
    final_bill = 20
elif size == 'l':
    final_bill = 25
else:
    print("You have to pick 'S', 'M' or 'L'\nSelect an available option.")
    exit()

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
if pepperoni == 'y' and size == 's':
    final_bill += 2
elif pepperoni == 'y' and (size == 'm' or size == 'l'):
    final_bill += 3
elif pepperoni == 'n':
    pass #do nothing
else:
    print("You have to pick 'Y' or 'N'\nSelect an available option.")
    exit()

extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
if extra_cheese == 'y':
    final_bill += 1
elif extra_cheese == 'n':
    pass #do nothing
else:
    print("You have to pick 'Y' or 'N'\nSelect an available option.")
    exit()

print(f"Your final bill is: ${final_bill}.")
