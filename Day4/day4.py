import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock, paper, scissors]

print("Welcome to Rock, Scissors or paper game!")
while 1:
    j = random.randint(0, 2)
    computer_hand = hand[j]
    user_hand = hand[(int(input("Type 1 to play rock, 2 to paper and 3 for scissors: "))) - 1]
    if computer_hand == rock and user_hand == rock:
        print("Players plays: ", rock)
        print("Computer plays: ", rock)
        print("That's a drawn.\n")
    elif computer_hand == rock and user_hand == scissors:
        print("Players plays: ", scissors)
        print("Computer plays: ", rock)
        print("You lose.\n")
    elif computer_hand == rock and user_hand == paper:
        print("Players plays: ", paper)
        print("Computer plays: ", rock)
        print("You won.\n")
    elif computer_hand == paper and user_hand == rock:
        print("Players plays: ", rock)
        print("Computer plays: ", paper)
        print("You lose.\n")
    elif computer_hand == paper and user_hand == scissors:
        print("Players plays: ", scissors)
        print("Computer plays: ", paper)
        print("You won.\n")
    elif computer_hand == paper and user_hand == paper:
        print("Players plays: ", paper)
        print("Computer plays: ", paper)
        print("That's a drawn.\n")
    elif computer_hand == scissors and user_hand == rock:
        print("Players plays: ", rock)
        print("Computer plays: ", scissors)
        print("You won.\n")
    elif computer_hand == scissors and user_hand == scissors:
        print("Players plays: ", scissors)
        print("Computer plays: ", scissors)
        print("That's a drawn.\n")
    elif computer_hand == scissors and user_hand == paper:
        print("Players plays: ", paper)
        print("Computer plays: ", scissors)
        print("You lose.\n")
