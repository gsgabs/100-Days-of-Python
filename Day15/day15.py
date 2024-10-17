from coffeeMachineMenu import MENU


def ask_coffee():
    coffees = ("espresso", "latte", "cappuccino", "report")
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while coffee_choice not in coffees:
        coffee_choice = input("Please choose one of the options on menu: espresso/latte/cappuccino: ").lower()
    return coffee_choice


coffee = ask_coffee()
if coffee == "report":
    print(MENU)




