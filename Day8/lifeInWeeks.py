def life_in_weeks(age):
    return (90 * 52) - (age * 52)


age_input = int(input("Tell me your age: "))
print(f"You have {life_in_weeks(age_input)} weeks left.\n")
