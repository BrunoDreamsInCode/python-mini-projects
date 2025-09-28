from art import logo
print(logo)

def find_highest_bidder(bidding_dictionary):
    # Initializing variables to store the winner
    higher_value = 0
    higher_name = ""

    # Finding the highest bidder
    for bidder in bidding_dictionary:
        if higher_value < bidding_dictionary[bidder]:
            higher_value = bidding_dictionary[bidder]
            higher_name = bidder

    # Showing the final result
    print(f"The winner is {higher_name} with a bid of ${higher_value}")

# Initializing the dictionary of auction players
auction_players = {}

# Condition to keep the script running
continue_bidding = True
while continue_bidding:
    name = input ("What is your name?: ")
    price = int(input("What is your bid?: $"))
    auction_players[name] = price

    # Input to either get the results or keep adding new bidders
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if should_continue == 'no':
        continue_bidding = False
    else:
        print("\n" * 20)

# Calling the function to output results
find_highest_bidder(auction_players)


