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

while run_program == 'yes':
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
            print("You went over! 😭")
            user_decision = 'n'
        else:
            user_decision = input("Type 'y' to get another card or type 'n' to pass: ").lower()

    if calculate_score(computer_hand) < 17:
        computer_hand.append(cards[random.randint(0, 13)])

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)
    print(f"\nYour final hand: {user_hand}, final score {user_score}")
    print(f"Computer final hand {computer_hand}, final score {computer_score}")
    if user_score > 21:
        print("You lose.")
    elif computer_score > 21:
        print("You won!")
    elif user_score == computer_score:
        print("It's a draw.")
    elif user_score > computer_score:
        print("You won!")
    elif computer_score > user_score:
        print("You lose.")

    run_program = input("Play again? Type 'yes' or 'no': ").lower()
    while run_program != 'yes' and run_program != 'no':
        run_program = input("Type yes or no: ").lower()
