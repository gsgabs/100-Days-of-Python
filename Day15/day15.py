from coffeeMachineMenu import MENU
from coffeeMachineMenu import resources


def ask_coffee():
    coffees = ("espresso", "latte", "cappuccino", "report", "off")
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while coffee_choice not in coffees:
        coffee_choice = input("Please choose one of the options on menu: espresso/latte/cappuccino: ").lower()
    return coffee_choice


money = 0.0
coffee = ask_coffee()
if coffee == "report":
    for resource, amount in resources.items():
        unit = "g" if resource == "coffee" else "ml"
        print(f"{resource.capitalize()}: {amount}{unit}")
    print(f"Money: ${money:.2f}")




