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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.10,
}


def report_generator():
    print("Current stock levels:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(resources['money'], 2)}")


def resource_problems(choice):
    problem_identified = "false"
    if MENU[choice]['ingredients']['water'] > resources['water']:
        problem_identified = "water"
    if MENU[choice]['ingredients']['coffee'] > resources['coffee']:
        problem_identified = "coffee"
    if 'milk' in MENU[choice]['ingredients']:
        if MENU[choice]['ingredients']['milk'] > resources['milk']:
            problem_identified = "milk"
    return problem_identified


def adding_funds():
    funds = 0
    print("Please insert coins.")
    funds += int(input("How many quarters? ")) * 0.25
    funds += int(input("How many dimes? ")) * 0.10
    funds += int(input("How many nickles? ")) * 0.05
    funds += int(input("How many pennies? ")) * 0.01
    return funds


def pricing(choice):
    return MENU[choice]['cost']


def resource_depleter(choice):
    resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    resources['water'] -= MENU[choice]['ingredients']['water']
    if 'milk' in MENU[choice]['ingredients']:
        resources['milk'] -= MENU[choice]['ingredients']['milk']


def coffee_loop():
    # 1. Prompt the user
    user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # 2. Turn off the coffee machine by entering 'off' to the prompt
    if user_selection != "off":

        # 3. Generate a report by entering 'report' to the prompt
        if user_selection == "report":
            report_generator()
            coffee_loop()

        # 4. Check resources sufficient.
        elif resource_problems(user_selection) != "false":
            print(f"Sorry there is not enough {resource_problems(user_selection)}")
            coffee_loop()

        # 5. Process coins
        else:
            wallet = adding_funds()
            cost = pricing(user_selection)

            # 6. Check if transaction is successful
            if not wallet >= cost:
                print("Sorry that's not enough money. Coins refunded.")
                coffee_loop()
            else:
                if wallet - cost > 0:
                    print(f"Here is ${round(wallet - cost, 2)} in change.")
                resources['money'] += MENU[user_selection]['cost']

                # 7. Make coffee and deplete ingredients.
                print(f"Here is your {user_selection} ☕️. Enjoy!")
                resource_depleter(user_selection)
                coffee_loop()
    else:
        print("Powering down the coffee machine.")


coffee_loop()
