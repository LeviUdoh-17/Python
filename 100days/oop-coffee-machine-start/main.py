from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while is_on:
    options = menu.get_items()
    MenuItem.name = input(f"What would you like? ({options}): ")
    choice = MenuItem.name

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_sufficient = coffee_maker.is_resource_sufficient(drink)
        if not is_sufficient:
            print("Sorry water not enough, money refunded.")
        else:
            cost = drink.cost
            payed = money_machine.make_payment(cost)
            if not payed:
                print("Sorry that's not enough money, money refunded")
            else:
                coffee_maker.make_coffee(drink)

