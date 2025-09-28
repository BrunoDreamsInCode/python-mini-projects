import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all_characters_mixed = letters + letters + symbols

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password? :"))
nr_symbols = int(input(f"How many symbols would you like? :"))
nr_numbers = int(input(f"How many numbers would you like? :"))
final_password_list_randomize = []
final_password = ''

##Creating the password letters
for variable in range(nr_letters):
    pass_letter_random = random.choice(letters)
    final_password_list_randomize.append(random.choice(letters))



##Creating the password symbols
for variable in range(nr_symbols):
    pass_letter_random = random.choice(symbols)
    final_password_list_randomize.append(random.choice(symbols))


##Creating the password numbers
for variable in range(nr_numbers):
    pass_letter_random = random.choice(numbers)
    final_password_list_randomize.append(random.choice(numbers))

#shuffling the list
random.shuffle(final_password_list_randomize)

#trading list to string output
for variable in range(nr_letters+nr_numbers+nr_symbols):
    final_password = "".join(final_password_list_randomize)

##output results
print(final_password)









