MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}
profit = 0
is_on, is_sufficient = True, True

def is_resource_sufficient(ingredients):
    for key, item in ingredients.items():
        if  item > resources[key]:
            print(f'Sorry there is not enough {key}')
            is_sufficient = False
            print(is_sufficient)
        else:
            return True
    return is_sufficient
def update_report(profit):
    profit += drink['cost']
    for key, item in ingredients.items():
        resources[key] -= item
    return profit

while is_on == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        ingredients = drink['ingredients']
        is_sufficient = is_resource_sufficient(ingredients)
        if is_sufficient == True:
            print("Insert coins")
            quaters = int(input("Quaters: "))
            dimes = int(input("Dimes: "))
            nickles = int(input("Nickles: "))
            penny = int(input("Pennies: "))
            total_value = 0.25*quaters + 0.1*dimes + 0.05*nickles + 0.01*penny
            # print(f"${total_value}")
            if total_value < drink['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif total_value > drink['cost']:
                profit += update_report(profit)
                change = total_value - drink['cost']
                print(f"Here is {round(change, ndigits= 2)} dollars in change.")
                print(f"Here is your {choice}. Enjoy!")
            else:
                profit += update_report(profit)
        else:
               break