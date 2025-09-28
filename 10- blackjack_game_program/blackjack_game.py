import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



cards_player_list = []
cards_bot_list = []


def buy_one_card(v1):
    random_value = random.choice(cards)
    v1.append(random_value)
    check_if_aces(v1)
    if sum(v1) > 21:
        check_who_won()

def check_if_aces(v1):
    for index, cards in enumerate(v1):
        if v1[index] == 11 and sum(v1) > 21:
            v1[index] = 1

def player_shows():
    print(f"\nYour cards: {cards_player_list}, current score: {sum(cards_player_list)}")

def bot_shows():
    print(f"Computer's first card: {cards_bot_list[0]}")

def bot_shows_first_card():
    print(f"Computer's first card: {cards_bot_list[0]}")

def check_who_won():
    print(f"\nYour final hand: {cards_player_list}, final score: {sum(cards_player_list)}")
    print(f"Computer's final hand: {cards_bot_list}, final score: {sum(cards_bot_list)}\n")

    game_over = False
    if sum(cards_player_list) == 21 and len(cards_player_list) == 2 and 11 in cards_player_list and sum(cards_bot_list) == 21 and len(cards_bot_list) == 2 and 11 in cards_bot_list:
        print("🤝 BOTH BLACKJACK! IT'S A DRAW!")
        game_over = True
    elif sum(cards_player_list) == 21 and len(cards_player_list) == 2 and 11 in cards_player_list:
        print("😎 BLACKJACK! YOU WIN!")
        game_over = True
    elif sum(cards_bot_list) == 21 and len(cards_bot_list) == 2 and 11 in cards_bot_list:
        print("💀 DEALER HAS BLACKJACK! YOU LOSE!")
        game_over = True
    elif sum(cards_player_list) > 21:
        print("🔥 YOU BUSTED!")
        game_over = True
    elif sum(cards_bot_list) > 21:
        print("💥 DEALER BUSTED! YOU WIN!")
        game_over = True
    elif sum(cards_player_list) == 21 and len(cards_player_list) == 2 and 11 in cards_player_list and sum(cards_bot_list) == 21 and len(cards_bot_list) == 2 and 11 in cards_bot_list:
        print("🤝 BOTH BLACKJACK! IT'S A DRAW!")
        game_over = True
    elif sum(cards_player_list) == 21 and len(cards_player_list) == 2 and 11 in cards_player_list:
        print("😎 BLACKJACK! YOU WIN!")
        game_over = True
    elif sum(cards_bot_list) == 21 and len(cards_bot_list) == 2 and 11 in cards_bot_list:
        print("💀 DEALER HAS BLACKJACK! YOU LOSE!")
        game_over = True
    elif sum(cards_player_list) > sum(cards_bot_list):
        print("🎉 YOU WIN!")
        game_over = True
    elif sum(cards_bot_list) > sum(cards_player_list):
        print("💀 YOU LOSE!")
        game_over = True
    if game_over == True:
        reset_game()
        game()

def check_player_busted():
    if sum(cards_player_list) > 21 or sum(cards_bot_list) > 21:
        check_who_won()

def reset_game():
    global cards_player_list, cards_bot_list, player_amount, bot_amount
    cards_player_list = []
    cards_bot_list = []
    player_amount = 0
    bot_amount = 0

def strategic_bot_buys(v1):
    lucky = 0
    while sum(cards_bot_list) < 17:
        buy_one_card(v1)


def game():
    wanna_play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if wanna_play == 'y':
        print(logo)
        buy_one_card(cards_player_list)
        buy_one_card(cards_player_list)
        buy_one_card(cards_bot_list)

        player_shows()
        bot_shows()

        if sum(cards_player_list) == 21 or sum(cards_bot_list) == 21:
            check_who_won()

        wanna_buy_another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
        while wanna_buy_another_card == 'y':
            buy_one_card(cards_player_list)
            if sum(cards_player_list) >= 21:
                check_who_won()
            player_shows()
            bot_shows()
            wanna_buy_another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
        if wanna_buy_another_card == 'n':
            strategic_bot_buys(cards_bot_list)
            check_who_won()
    else:
        print("Bye!")


game()

