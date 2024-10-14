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
    index = random.randint(0, 50)
    return games[index]


game_1 = generate_random_game()
game_2 = generate_random_game()

while game_1["year"] == game_2["year"] or game_1["name"] == game_2["name"]:
    print(game_1, game_2)
    game_2 = generate_random_game()
print(game_1, game_2)









