from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True


while is_on:

    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    user_selection = input(f"What would you like? ({menu.get_items()}): ").lower()

    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_selection != "off":

        # 3. Print report.
        if user_selection == "report":
            coffee_maker.report()
            money_machine.report()

        # 4. Check resources sufficient?
        else:
            item = menu.find_drink(user_selection)
            is_possible = coffee_maker.is_resource_sufficient(item)

            # 5. Process coins.
            if is_possible:
                payment_successful = money_machine.make_payment(item.cost)

                # 6.   Check transaction successful?
                if payment_successful:

                    # 7. Make coffee
                    coffee_maker.make_coffee(item)

    # 2 Continued
    else:
        print("Powering down the coffee machine.")
        is_on = False
