from coffeeMachineMenu import MENU
from coffeeMachineMenu import resources


def ask_coffee():
    coffees = ("espresso", "latte", "cappuccino", "report", "off")
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while coffee_choice not in coffees:
        coffee_choice = input("Please choose one of the options on menu: espresso/latte/cappuccino: ").lower()
    return coffee_choice


def resources_available(coffee_choice):
    enough_resources = True
    for ingredient in MENU[coffee_choice]["ingredients"]:
        if MENU[coffee_choice]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Not enough {ingredient}")
            enough_resources = False
    return enough_resources


def use_resources(coffee_choice):
    for ingredient in MENU[coffee_choice]["ingredients"]:
        resources[ingredient] -= MENU[coffee_choice]["ingredients"][ingredient]


money = 0.0
coffee = ''

while coffee != "off":
    coffee = ask_coffee()
    if coffee == "report":
        for resource, amount in resources.items():
            unit = "g" if resource == "coffee" else "ml"
            print(f"{resource.capitalize()}: {amount}{unit}")
        print(f"Money: ${money:.2f}")
        continue
    if coffee != "off":
        if not resources_available(coffee):
            print("refund")
            continue
        print(f"Here's your {coffee}. Enjoy!")
        use_resources(coffee)









