from controllers.CoffeeMachine import CoffeeMachine

coffee_machine = CoffeeMachine()
is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        print("Turning machine off.")
        is_on = False
    elif user_choice == "report":
        coffee_machine.print_report()
    elif user_choice in ['espresso', 'latte', 'cappuccino']:
        if not coffee_machine.check_sufficient_resources(user_choice):
            continue

        coins_provided = coffee_machine.get_user_coins()
        total_money = coffee_machine.check_coins_provided(coins_provided)
        if not coffee_machine.check_successful_transaction(total_money):
            continue

        coffee_machine.make_coffee()
    elif user_choice == "replenish":
        coffee_machine.replenish_machine()
    else:
        print("That's not an available option.")