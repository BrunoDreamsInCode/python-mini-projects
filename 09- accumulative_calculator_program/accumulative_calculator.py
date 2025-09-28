from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def do_calc(option,n1,n2):
    return dictionary_calculator[option](n1, n2)


dictionary_calculator = {
    "+": add,
    "-": sub,
    "*": mult,
    "/":divide,
}


while True:
    print(logo)
    first_number = float(input("Whats your first number? "))
    should_continue = True

    while should_continue:
        option_calc = input("+\n-\n*\n/\nPick an option:  ")
        second_number = float(input("Whats the next number? "))

        result = do_calc(option_calc,first_number,second_number)

        print(f"{first_number} {option_calc} {second_number} = {result}")

        yes_or_no = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if yes_or_no == 'y':
            first_number = result
        elif yes_or_no == 'n':
            print("\n" * 20)
            should_continue = False
        else:
            print("\n" * 20)
            should_continue = False
