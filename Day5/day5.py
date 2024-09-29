import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print(len(letters))

user_choice = input("Type Y to generate a password or N to finish the program: ")

while user_choice == "y" or user_choice == "Y":
    password = []
    print(password)

    letter_quantity = random.randint(6, 10)
    for j in range(0, letter_quantity):
        index = random.randint(0, 51)
        password.append(letters[index])

    number_quantity = random.randint(4, 6)
    for j in range(0, number_quantity):
        index = random.randint(0, 9)
        password.append(numbers[index])

    symbols_quantity = random.randint(2, 4)
    for j in range(0, symbols_quantity):
        index = random.randint(0, 8)
        password.append(symbols[index])

    random.shuffle(password)
    password_string = ''.join(password)

    print(password)
    print(password_string)
    user_choice = input("Type Y to generate a password or N to finish the program: ")
