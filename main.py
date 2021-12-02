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
    "money": 0
}

machine_on = True

while machine_on:
    drink_ordered = input("What would you like? (espresso/latte/cappuccino): ")

    if drink_ordered == "off":
        machine_on = False

    if drink_ordered == "report":
        machine_on = False
        for key, value in resources.items():
            print(key, ' : ', value)

    if drink_ordered == "espresso":
        if resources['water'] >= MENU["espresso"]["ingredients"]["water"] and resources['coffee'] >= MENU["espresso"]["ingredients"]["coffee"]:
            print("Please insert coins: ")
            money_in_quarters = int(input("How many quarters?: ")) * 0.25
            money_in_dimes = int(input("How many dimes?: ")) * 0.10
            money_in_nickles = int(input("How many nickles?: ")) * 0.05
            money_in_pennies = int(input("How many pennies?: ")) * 0.01
            total_money_put_in = money_in_quarters + money_in_dimes + money_in_nickles + money_in_pennies

            if total_money_put_in >= (MENU["espresso"]["cost"]):
                resources['money'] += MENU["espresso"]["cost"]
                money_back = total_money_put_in - MENU["espresso"]["cost"]
                print(f"Here is your change: ${money_back}")

                water_in_reservoir = resources['water']
                water_req_espresso = MENU["espresso"]["ingredients"]["water"]
                water_left = water_in_reservoir - water_req_espresso
                resources['water'] = water_left

                coffee_in_reservoir = resources['coffee']
                coffee_req_espresso = MENU["espresso"]["ingredients"]["coffee"]
                coffee_left = coffee_in_reservoir - coffee_req_espresso
                resources['coffee'] = coffee_left

                print(" ")
                print("Here is your espresso. Enjoy! ☕️\n")
                print("Water left in machine: ", resources['water'], "mL\n")
                print("Coffee left in machine: ", resources['coffee'], "mL\n")

            else:
                print(f"You put in ${total_money_put_in}, this is not enough to cover the cost. Goodbye.")
                machine_on = False
                for key, value in resources.items():
                    print(key, ' : ', value)

        elif resources['water'] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.\n")
            machine_on = False
            print("Resources and Money Balance is: \n")
            for key, value in resources.items():
                print(key, ' : ', value)

        else:
            if resources['coffee'] < MENU["espresso"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.\n")
                machine_on = False
                print("Resources and Money Balance is: \n")
                for key, value in resources.items():
                    print(key, ' : ', value)

    if drink_ordered == "latte":
        if resources['water'] >= MENU["latte"]["ingredients"]["water"] and resources['coffee'] >= MENU["latte"]["ingredients"]["coffee"] and resources['milk'] >= MENU["latte"]["ingredients"]["milk"]:
            print("Please insert coins: ")
            money_in_quarters = int(input("How many quarters?: ")) * 0.25
            money_in_dimes = int(input("How many dimes?: ")) * 0.10
            money_in_nickles = int(input("How many nickles?: ")) * 0.05
            money_in_pennies = int(input("How many pennies?: ")) * 0.01
            total_money_put_in = money_in_quarters + money_in_dimes + money_in_nickles + money_in_pennies

            if total_money_put_in >= (MENU["latte"]["cost"]):
                resources['money'] += MENU["latte"]["cost"]
                money_back = total_money_put_in - MENU["latte"]["cost"]
                print(f"\nHere is your change: ${money_back}")

                water_in_reservoir = resources['water']
                water_req_latte = MENU["latte"]["ingredients"]["water"]
                water_left = water_in_reservoir - water_req_latte
                resources['water'] = water_left

                coffee_in_reservoir = resources['coffee']
                coffee_req_latte = MENU["latte"]["ingredients"]["coffee"]
                coffee_left = coffee_in_reservoir - coffee_req_latte
                resources['coffee'] = coffee_left

                milk_in_reservoir = resources['milk']
                milk_req_latte = MENU["latte"]["ingredients"]["milk"]
                milk_left = milk_in_reservoir - milk_req_latte
                resources['milk'] = milk_left

                print("\nHere is your latte. Enjoy! ☕️\n")
                print("Water left in machine: ", resources['water'], "mL")
                print("Milk left in machine: ", resources['milk'], "mL")
                print("Coffee left in machine: ", resources['coffee'], "mL\n")

            else:
                print(f"You put in ${total_money_put_in}, this is not enough to cover the cost. Goodbye.")
                machine_on = False
                for key, value in resources.items():
                    print(key, ' : ', value)

        elif resources['water'] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.\n")
            machine_on = False
            print("Resources and Money Balance is: \n")
            for key, value in resources.items():
                print(key, ' : ', value)

        elif resources['milk'] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.\n")
            machine_on = False
            print("Resources and Money Balance is: \n")
            for key, value in resources.items():
                print(key, ' : ', value)

        else:
            if resources['coffee'] < MENU["latte"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.\n")
                machine_on = False
                print("Resources and Money Balance is: \n")
                for key, value in resources.items():
                    print(key, ' : ', value)

    if drink_ordered == "cappuccino":
        if resources['water'] >= MENU["cappuccino"]["ingredients"]["water"] and resources['coffee'] >= MENU["cappuccino"]["ingredients"]["coffee"] and resources['milk'] >= MENU["cappuccino"]["ingredients"]["milk"]:
            print("Please insert coins: ")
            money_in_quarters = int(input("How many quarters?: ")) * 0.25
            money_in_dimes = int(input("How many dimes?: ")) * 0.10
            money_in_nickles = int(input("How many nickles?: ")) * 0.05
            money_in_pennies = int(input("How many pennies?: ")) * 0.01
            total_money_put_in = money_in_quarters + money_in_dimes + money_in_nickles + money_in_pennies

            if total_money_put_in >= (MENU["cappuccino"]["cost"]):
                resources['money'] += MENU["cappuccino"]["cost"]
                money_back = total_money_put_in - MENU["cappuccino"]["cost"]
                print(f"\nHere is your change: ${money_back}")

                water_in_reservoir = resources['water']
                water_req_cappuccino = MENU["cappuccino"]["ingredients"]["water"]
                water_left = water_in_reservoir - water_req_cappuccino
                resources['water'] = water_left

                coffee_in_reservoir = resources['coffee']
                coffee_req_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]
                coffee_left = coffee_in_reservoir - coffee_req_cappuccino
                resources['coffee'] = coffee_left

                milk_in_reservoir = resources['milk']
                milk_req_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]
                milk_left = milk_in_reservoir - milk_req_cappuccino
                resources['milk'] = milk_left

                print("\nHere is your cappuccino. Enjoy! ☕️\n")
                print("Water left in machine: ", resources['water'], "mL")
                print("Milk left in machine: ", resources['milk'], "mL")
                print("Coffee left in machine: ", resources['coffee'], "mL\n")

            else:
                print(f"You put in ${total_money_put_in}, this is not enough to cover the cost. Goodbye.")
                machine_on = False
                for key, value in resources.items():
                    print(key, ' : ', value)

        elif resources['water'] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.\n")
            machine_on = False
            print("Resources and Money Balance is: \n")
            for key, value in resources.items():
                print(key, ' : ', value)

        elif resources['milk'] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.\n")
            machine_on = False
            print("Resources and Money Balance is: \n")
            for key, value in resources.items():
                print(key, ' : ', value)

        else:
            if resources['coffee'] < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.\n")
                machine_on = False
                print("Resources and Money Balance is: \n")
                for key, value in resources.items():
                    print(key, ' : ', value)

