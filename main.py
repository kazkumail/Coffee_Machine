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

def check_charge(ctype):
    if resources['water'] >= MENU[ctype]["ingredients"]["water"] and resources['coffee'] >= MENU[ctype]["ingredients"]["coffee"]:
        print("Please insert coins: ")
        money_in_quarters = int(input("How many quarters?: ")) * 0.25
        money_in_dimes = int(input("How many dimes?: ")) * 0.10
        money_in_nickles = int(input("How many nickles?: ")) * 0.05
        money_in_pennies = int(input("How many pennies?: ")) * 0.01
        total_money_put_in = float(money_in_quarters) + money_in_dimes + money_in_nickles + money_in_pennies

        if total_money_put_in >= (MENU[ctype]["cost"]):
            resources['money'] += MENU[ctype]["cost"]
            money_back = round(total_money_put_in - MENU[ctype]["cost"],2)
            print(f"Here is your change: ${money_back}")

            water_in_reservoir = resources['water']
            water_req_espresso = MENU[ctype]["ingredients"]["water"]
            water_left = water_in_reservoir - water_req_espresso
            resources['water'] = water_left

            coffee_in_reservoir = resources['coffee']
            coffee_req_espresso = MENU[ctype]["ingredients"]["coffee"]
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

    elif resources['water'] < MENU[ctype]["ingredients"]["water"]:
        print("Sorry there is not enough water.\n")
        machine_on = False
        print("Resources and Money Balance is: \n")
        for key, value in resources.items():
            print(key, ' : ', value)

    else:
        if resources['coffee'] < MENU[ctype]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.\n")
            machine_on = False
            print("Resources and Money Balance is: \n")
            for key, value in resources.items():
                print(key, ' : ', value)
                
machine_on = True

while machine_on:
    drink_ordered = input("What would you like? (espresso/latte/cappuccino): ")

    if drink_ordered == "off":
        machine_on = False

    if drink_ordered == "report":
        for key, value in resources.items():
            print(key, ' : ', value)
        

    if drink_ordered == "espresso":
        check_charge(drink_ordered)
        
    if drink_ordered == "latte":
        check_charge(drink_ordered)
        
    if drink_ordered == "cappuccino":
        check_charge(drink_ordered)
        
