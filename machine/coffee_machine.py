# JetBrain Academy first project
class CoffeeMachine:

    def __init__(self):
        self.water_qty = 400
        self.milk_qty = 540
        self.coffee_qty = 120
        self.cups_qty = 9
        self.money_qty = 550

        # buy, fill, take, remaining, exit
        # choose_action
        # buy_action
        # fill_action
        # take_action
        self.set_initial_state()

    def print_buy_prompt(self):
        print("What do you want to buy? "
              "1 - espresso, "
              "2 - latte, "
              "3 - cappuccino:")

    def set_initial_state(self):
        self.state = "choose_action"
        self.fill_state = "water"
        self.print_action()

    def execute_action(self, action):
        if self.state == "choose_action":
            self.choose_action(action)
        # 1 - espresso, 2 - latte, 3 - cappuccino
        elif self.state == "buy_action":
            self.buy_action(action)
        elif self.state == "fill_action":
            self.fill_action(action)
        elif self.state == "take_action":
            self.take_action(action)

    def choose_action(self, action):
        if action == "remaining":
            self.print_qty()
            self.print_action()
        elif action == "buy":
            self.state = "buy_action"
            self.print_buy_prompt()
        elif action == "fill":
            self.state = "fill_action"
            self.fill_state = "water"
            self.print_fill_state()
        elif action == "take":
            self.take_action()
            self.print_action()

    def buy_action(self, action):
        water_qty_left = 0
        milk_qty_left = 0
        coffee_qty_left = 0
        cups_qty_left = 0
        money_qty_left = 0
        drink_type = action

        if drink_type == "1":
            water_qty_left = self.water_qty - 250
            # milk_qty -= 0
            coffee_qty_left = self.coffee_qty - 16
            cups_qty_left = self.cups_qty - 1
            money_qty_left = self.money_qty + 4
        elif drink_type == "2":
            water_qty_left = self.water_qty - 350
            milk_qty_left = self.milk_qty - 75
            coffee_qty_left = self.coffee_qty - 20
            cups_qty_left = self.cups_qty - 1
            money_qty_left = self.money_qty + 7
        elif drink_type == "3":
            water_qty_left = self.water_qty - 200
            milk_qty_left = self.milk_qty - 100
            coffee_qty_left = self.coffee_qty - 12
            cups_qty_left = self.cups_qty - 1
            money_qty_left = self.money_qty + 6

        if water_qty_left <= 0:
            print("Sorry, not enough water!")
        elif coffee_qty_left <= 0:
            print("Sorry, not enough coffee!")
        elif milk_qty_left <= 0 and drink_type == 3:
            print("Sorry, not enough milk!")
        elif cups_qty_left <= 0:
            print("Sorry, not enough cups!")
        else:
            self.water_qty = water_qty_left
            if milk_qty_left != 0:
                self.milk_qty = milk_qty_left
            self.coffee_qty = coffee_qty_left
            self.cups_qty = cups_qty_left
            self.money_qty = money_qty_left
            print("I have enough resources, making you a coffee!")

        self.set_initial_state()

    def print_qty(self):
        print("The coffee machine has:")
        print("%s of water" % self.water_qty)
        print("%s of milk" % self.milk_qty)
        print("%s of coffee beans" % self.coffee_qty)
        print("%s of disposable cups" % self.cups_qty)
        print("%s of money" % self.money_qty)
        print("")

    def print_fill_state(self):
        if self.fill_state == "water":
            print("Write how many ml of water do you want to add:")
        if self.fill_state == "milk":
            print("Write how many ml of milk do you want to add:")
        if self.fill_state == "coffee":
            print("Write how many grams of coffee beans do you want to add:")
        if self.fill_state == "cups":
            print("Write how many disposable cups of coffee do you want to add:")

    def fill_action(self, action):
        if self.fill_state == "water":
            self.water_qty += int(action)
            self.fill_state = "milk"
        elif self.fill_state == "milk":
            self.milk_qty += int(action)
            self.fill_state = "coffee"
        elif self.fill_state == "coffee":
            self.coffee_qty += int(action)
            self.fill_state = "cups"
        elif self.fill_state == "cups":
            self.cups_qty += int(action)
            self.set_initial_state()
            return
        self.print_fill_state()
        return

    def take_action(self):
        print("I gave you %s" % self.money_qty)
        self.money_qty = 0

    def print_action(self):
        print("Write action (buy, fill, take, remaining, exit):")


coffee_machine = CoffeeMachine()

while True:
    action = input("> ")
    if action == "exit":
        break
    coffee_machine.execute_action(action)
