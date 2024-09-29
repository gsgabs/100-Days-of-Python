print("\n\nWelcome to treasure maze! Your mission is find the treasure.\n")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("\nYou're at a cross road. Where do you want to go?")
if input("Type left or right: ") == "left":
    print("You were run over, game over")
else:
    print("You've come to a lake. What do you want to do?")
    if input("swin or to fish? ") == "swin":
        print("The crocodiles got you, game over")
    else:
        print("You fished a key. What do you want to do?")
        while input("keep fishing or look for a door? ") == "keep fishing":
            print("You fished nothing")
        print("You found two doors. Which do you wanna open?")
        door = input("stone, wood or steel? ")
        if door == "stone":
            print("You found the Treasure! Congratulations.")
        elif door == "wood":
            print("You were cursed. Game over")
        else:
            print("You found the exit of the maze, good job")
