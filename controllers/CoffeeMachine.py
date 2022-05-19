from menu import MENU, resources


class CoffeeMachine:
    def __init__(self):
        self.resources = resources
        self.replenish_resources = {'water': False, 'coffee': False, 'milk': False}
        self.money = 0.00
        self.selected_coffee = ""
        self.selected_coffee_ingredients = {}
        self.selected_coffee_price = 0.00

    def print_report(self):
        water, milk, coffee = self.resources.values()
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${self.money}")

    def check_sufficient_resources(self, coffee_choice):
        self.selected_coffee = coffee_choice
        self.selected_coffee_ingredients = MENU[coffee_choice]["ingredients"]
        missing_ingredients = []
        for ingredient in resources.keys():
            if ingredient not in  self.selected_coffee_ingredients:
                continue
            if resources[ingredient] < self.selected_coffee_ingredients[ingredient]:
                missing_ingredients.append(ingredient)
        if len(missing_ingredients) == 0:
            self.selected_coffee_price = MENU[coffee_choice]["cost"]
            print(f"The cost of an {coffee_choice} is ${self.selected_coffee_price}")
            return True
        error_msg = f"Sorry, there is not enough"
        for i in range(len(missing_ingredients)):
            self.replenish_resources[missing_ingredients[i]] = True
            if len(missing_ingredients) == 2:
                error_msg += f" {missing_ingredients[0]} and {missing_ingredients[1]}."
                break
            if i == len(missing_ingredients) - 1:
                error_msg += f" and {missing_ingredients[i]}."
            else:
                error_msg += f" {missing_ingredients[i]},"
        print(error_msg)
        return False

    def get_user_coins(self):
        coins_provided = {'pennies': 0, 'nickles': 0, 'dimes': 0, 'quarters': 0}
        coins_provided['pennies'] += int(input('How many pennies would you like to use?: '))
        coins_provided['nickles'] += int(input('How many nickles would you like to use?: '))
        coins_provided['dimes'] += int(input('How many dimes would you like to use?: '))
        coins_provided['quarters'] += int(input('How many quarters would you like to use?: '))
        return coins_provided

    def check_coins_provided(self, coins_provided):
        money_provided = 0
        for coin in coins_provided:
            if coin == 'pennies':
                money_provided += coins_provided[coin] * 0.01
            elif coin == 'nickles':
                money_provided += coins_provided[coin] * 0.05
            elif coin == 'dimes':
                money_provided += coins_provided[coin] * 0.10
            else:
                money_provided += coins_provided[coin] * 0.25
        return money_provided

    def check_successful_transaction(self, money_provided):
        if money_provided < self.selected_coffee_price:
            error_message = f"Sorry, that's not enough money. You are ${self.selected_coffee_price - money_provided} short."
            print(error_message) if money_provided == 0 else print(error_message + " Refunding you now.")
            return False
        else:
            self.money += self.selected_coffee_price
            if money_provided > self.selected_coffee_price:
                change = money_provided - self.selected_coffee_price
                print(f"Here is ${round(change, 2)} dollars in change.")
            return True

    def make_coffee(self):
        for ingredient in self.selected_coffee_ingredients:
            self.resources[ingredient] -= self.selected_coffee_ingredients[ingredient]
        print(f"Here is your {self.selected_coffee}. Enjoy!")

    def replenish_machine(self):
        for ingredient in self.replenish_resources:
            if self.replenish_resources[ingredient]:
                if ingredient == 'water':
                    self.resources['water'] = 300
                if ingredient == 'coffee':
                    self.resources['coffee'] = 100
                if ingredient == 'milk':
                    self.resources['milk'] = 200
                self.replenish_resources[ingredient] = False

