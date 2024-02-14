from menu import Menu, MenuItem
from coffe_maker import CoffeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffe_maker = CoffeMaker()
menu = Menu()
coffe_maker.report()
money_machine.report()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"wt would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
             coffe_maker.make_coffee(drink)


