from art import logo
import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(player_cards):
    player_score = 0
    for item in player_cards:
        player_score += item
    return player_score


def generate_deck():
    deck = []
    for i in range(0, 2):
        index = random.randint(0, 13)
        deck.append(cards[index])
    return deck


run_program = input("Star the game? Type 'yes' or 'no': ").lower()
while run_program != 'yes' and run_program != 'no':
    run_program = input("Type yes or no: ").lower()

if run_program == 'yes':
    print(logo)
    user_hand = generate_deck()
    computer_hand = generate_deck()

    print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand)}")
    print(f"Computer firs card: {computer_hand[0]}")

    user_decision = input("Type 'y' to get another card or type 'n' to pass: ").lower()
    while user_decision == 'y':
        user_hand.append(cards[random.randint(0, 13)])
        print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand)}")
        if calculate_score(user_hand) > 21:
            print("You went over!")
            user_decision = 'n'
        user_decision = input("Type 'y' to get another card or type 'n' to pass: ").lower()


