from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()

money=MoneyMachine()
coffe=CoffeeMaker()
is_on=True
while is_on:

    options=menu.get_items()
    choice=input(f"what would you like {options} :")
    if choice=='off':
        is_on=False
    elif choice=='report':
        coffe.report()
        money.report()
    else:
        drink=menu.find_drink(choice)
        if coffe.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffe.make_coffee(drink)
             
