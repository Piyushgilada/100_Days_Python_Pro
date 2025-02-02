import sys

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item=Menu()
coin_machine=MoneyMachine()
coffee_machine=CoffeeMaker()

is_continue=True
while is_continue:
    options=menu_item.get_items()
    choice=input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if choice=='report':
        coffee_machine.report()
        coin_machine.report()
    elif choice == 'off':
        sys.exit()
    else:
        drink=menu_item.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and coin_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)



