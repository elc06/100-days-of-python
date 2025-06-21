import random

logo = r"""
.------.            _     _            _    _            _                                      
|A_  _ |.          | |   | |          | |  (_)          | |                                     
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __                                  
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /                                  
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <                                   
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\                                 
      |  \/ K|                            _/ |                                                  
      `------'                           |__/                                                   
"""
print(logo)
print("Welcome to Blackjack Game!\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def set_of_cards():
    return [random.choice(cards), random.choice(cards)]


def calculate_score(card_list):
    score = sum(card_list)
    # Adjust Ace from 11 to 1 if over 21
    while score > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
        score = sum(card_list)
    return score


def compare_scores(player_score, dealer_score):
    if player_score > 21:
        return "You went over 21. You lose."
    elif dealer_score > 21:
        return "Dealer went over 21. You win!"
    elif player_score == dealer_score:
        return "Draw!"
    elif player_score == 21:
        return "Blackjack! You win!"
    elif dealer_score == 21:
        return "Dealer has Blackjack. You lose."
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose."


def dealer_turn(dealer_cards):
    print(f"\nDealer's turn:")
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        print(f"Dealer draws: {dealer_cards} -> Score: {calculate_score(dealer_cards)}")
    return dealer_cards


def player_turn(player_cards, dealer_cards):
    while True:
        player_score = calculate_score(player_cards)
        print(f"\nYour cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 21:
            print("You hit Blackjack!")
            break
        if player_score > 21:
            print("You bust! Over 21.")
            break

        choice = input("Type 'h' to hit or 's' to stand: ").lower()
        if choice == 'h':
            player_cards.append(random.choice(cards))
        elif choice == 's':
            print(f"\nYou stand with cards: {player_cards}, final score: {player_score}")
            break
        else:
            print("Invalid input. Please type 'h' or 's'.")
    return player_cards


# Game loop
while True:
    game_mode = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_mode == 'y':
        player_cards = set_of_cards()
        dealer_cards = set_of_cards()

        player_cards = player_turn(player_cards, dealer_cards)
        player_score = calculate_score(player_cards)

        if player_score <= 21:
            dealer_cards = dealer_turn(dealer_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"\nFinal Results:")
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print(compare_scores(player_score, dealer_score))

    elif game_mode == 'n':
        print("Thanks for playing! Bye bye.")
        break
    else:
        print("Invalid input. Please type 'y' or 'n'.")
