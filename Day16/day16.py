from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def ask_coffee():
    coffees = Menu.get_items() + "report" + "off"
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while coffee_choice not in coffees:
        coffee_choice = input("Please choose one of the options on menu: espresso/latte/cappuccino: ").lower()
    return coffee_choice


def report():
    MoneyMachine.report()
    CoffeeMaker.report()


while True:
    coffee = ask_coffee()
    if coffee == "off":
        print("Turning off the coffee machine🫡. Goodbye!")
        break
    if coffee == "report":
        report()
        continue
