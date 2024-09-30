def calculate_love_score(name1, name2):
    couple_name = (name1 + name2).lower()
    true_quantity = 0
    love_quantity = 0

    for letter_name in couple_name:
        for letter_true in "true":
            if letter_name == letter_true:
                true_quantity += 1
        for letter_love in "love":
            if letter_name == letter_love:
                love_quantity += 1
    return str(true_quantity) + str(love_quantity)


user_name = input("What's your name: ").lower()
loved_name = input("Name of the person you like: ").lower()

print(f"Love score of this couple is : {int(calculate_love_score(user_name, loved_name))}")
