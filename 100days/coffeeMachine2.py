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

profit = 0

def is_resource_sufficient(order_ingredient):
    """Returns true when order can be made, and false when ingredient is insufficient"""
    for items in order_ingredient:
        if order_ingredient[items] >= resources[items]:
            print(f"Sorry there's not enough {items}.")
            return False
    return True

def process_coins():
    """returns the total calculated from coins inserted"""
    print("please insert coins.")
    total = int(input("How many quaters?: "))*0.25 + int(input("How many dimes?: "))*0.1 + int(input("How many nickles?: "))*0.05 + int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Returns true when the payment is accepted, and false when the funds are insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change") 
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, money refunded.")
        return False
def make_coffee(drink_name, order_ingredient):
    """Deduct required ingredient from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here's your {drink_name} ☕")

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"]) 