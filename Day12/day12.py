from random import randint

logo = """
    
  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       

    """

print(logo)
print("Welcome to the number guessing Game!")
print("I'm thinking in a number beteween 1 and 100.")
difficulty = input("Choose the difficulty, type 'easy' or 'hard': ").lower()
while difficulty != 'easy' and difficulty != 'hard':
    input("Choose the difficulty, type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    hearts = 10
elif difficulty == 'hard':
    hearts = 5
the_number = randint(1, 100)
guess = -1
while guess != the_number and hearts > 0:
    guess = int(input("Make a guess:  "))
    if guess > the_number:
        print("Too high.")
    if guess < the_number:
        print("Too low.")
    if guess != the_number:
        hearts -= 1

if guess == the_number:
    print(f"\nYou got it! The answer was {the_number}.\n\n\n")
else:
    print("\nYou've run out of guesses, you lose.\n\n\n")

