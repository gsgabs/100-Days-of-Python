import random
from gameLibrary import games

logo = """
    
  ___ ___ .__       .__                  
 /   |   \|__| ____ |  |__   ___________ 
/    ~    \  |/ ___\|  |  \_/ __ \_  __ 
\    Y    /  / /_/  >   Y  \  ___/|  | \/
 \___|_  /|__\___  /|___|  /\___  >__|   
       \/   /_____/      \/     \/       
                                         
___  ________                            
\  \/ /  ___/                            
 \   /\___ \                             
  \_//____  >                            
          \/                             
.____                                    
|    |    ______  _  __ ___________      
|    |   /  _ \ \/ \/ // __ \_  __ \     
|    |__(  <_> )     /\  ___/|  | \/     
|_______ \____/ \/\_/  \___  >__|        
        \/                 \/            

    """

print(logo)


def generate_random_game():
    index = random.randint(0, 51)
    return games[index]


print("Welcome to HigherVsLower game")
print("You'll have to guess which from the two presented games was released earlier.")
print("Let's get started!\n")
streak = 0
game_over = False

while not game_over:
    game_1 = generate_random_game()
    game_2 = generate_random_game()

    while game_1["year"] == game_2["year"] or game_1["name"] == game_2["name"]:
        print(game_1, game_2)
        game_2 = generate_random_game()

    print(f"Which was released earlier: {game_1['name']} or {game_2['name']}")
    guess = input(f"Type 1 for {game_1['name']} or 2 for {game_2['name']}: ")

    while (guess != '1' and guess != '2') and (guess != game_1['name'] and guess != game_2['name']):
        print(f"Type 1 for {game_1['name']} or 2 for {game_2['name']}. ")
        guess = input("You can also type the game name: ")
    if guess == game_1['name']:
        guess = 1
    if guess == game_2['name']:
        guess = 2

    if game_1['year'] < game_2['year']:
        primeiro = game_1
    if game_2['year'] < game_1['year']:
        primeiro = game_2

    if guess == primeiro:
        streak += 1
        print(f"Well done! Streak +1   total{streak}")
    else:
        print("Nooo 😭 ")





