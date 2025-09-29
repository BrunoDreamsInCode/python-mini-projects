import random
from art import logo

# Return a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculate the sum of a player's or computer's cards.
# Convert Ace(s) from 11 to 1 if the total exceeds 21.
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Return the final result as a string
def compare (cards_player,cards_computer):
    if cards_player > 21:
        return "You went over. You lose 😭"
    elif cards_computer > 21:
        return "Opponent went over. You win 😁"
    elif cards_player == cards_computer:
        return "Draw 🙃"
    elif cards_player == 0:
        return "Win with a Blackjack 😎"
    elif cards_computer == 0:
        return "Lose, opponent has Blackjack 😱"
    elif cards_computer > cards_player:
        return "You lose 😤"
    elif cards_player > cards_computer:
        return "You win 😃"

# Main game function
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    # Deal the first two cards to the player and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Main game loop: continues until the game ends (Blackjack, bust, or player passes)
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # If score is 0, the player has a Blackjack.
        # Convert it to 21 for display purposes.
        if user_score == 0:
            print(f"\nYour cards: {user_cards}, current score: 21")
        else:
            print(f"\nYour cards: {user_cards}, current score: {user_score}")

        # Computer has 2 cards, but only the first one is shown according to the game rules
        print(f"Computer's first card: {computer_cards[0]}")

        # A score of 0 indicates Blackjack.
        # End the game if either player has Blackjack or the user busts.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the player if they want to draw another card
            user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
            # End the game when the player chooses not to draw another card
                is_game_over = True

    # Computer draws cards until its score reaches 17 or higher, unless it has Blackjack
    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show the player's final hand and score
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")

    # Show the computer's final hand and score
    # If the computer has Blackjack (score = 0), display 21
    if computer_score == 0:
        print(f"Computer's final hand: {computer_cards}, final score: 21")
    else:
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Display the result of the game
    print(f"\n{compare(user_score, computer_score)}\n")



# Main loop to ask the player if they want to play another game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    # Clear the screen before starting a new game
    print("\n"*20)
    play_game()

# Print goodbye message when player decides to quit
print("Bye!")



