#   Coffee machine program layout
    #1. Display welcome messages and logo.
    #2. Show the coffe menu with prices.
    #3. Prompt the user to choose a drink.
    #4. Repeat the order and show the drink price.
    #5. Check if there are enough resources to make the selected drink.
    #   -If not enough, print a warning and return to the menu.
    #6. Ask the user to insert coins:
    #   -How many quarters?:
    #   -How many dimes?
    #   -How many nickles?
    #   -How many pennies?
    #7. Calculate the total inserted.
    #8. If payment is insufficient:
    #   -Refund.
    #9. If payment is sufficient:
    #   -Give change if needed.
    #   -Deduct ingredients from machine resources.
    #   -Serve the coffee.
    #10. Display thank you/enjoy message.
    #11. Loop back to step 3 (unless the user turns off the machine)
    #12. If user enter 'off', shut down the machine.

#   Project to-do list
#   TODO: 1. Prompt user for input
#   TODO: 2. Handle 'off' command to shut down machine
#   TODO: 3. Print machine report, 'info'
#   TODO: 4. Check resources availability
#   TODO: 5. Process coin input
#   TODO: 6. Validate if transaction is successful
#   TODO: 7. Make coffee and deduct resources

#  Menu of the coffee machine
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

# Coffee machine storage
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Machine LOGO
logo = r'''         ____       __  __             __  __           _             
        / ___|___  / _|/ _| ___  ___  |  \/  | __ _ ___| |_ ___ _ __  
       | |   / _ \| |_| |_ / _ \/ _ \ | |\/| |/ _` / __| __/ _ | '__| 
       | |__| (_) |  _|  _|  __|  __/ | |  | | (_| \__ | ||  __| |    
        \____\___/|_| |_|  \___|\___| |_|  |_|\__,_|___/\__\___|_|'''

coffee_mug = r"""                   )  (
                 (    ) )
                    )   ( (
                mrf_______)_
                .-'---------|  
               ( C|/\/\/\/\/|
                '-./\/\/\/\/|
                  |_________'
                   '-------'"""

#Machine Menu
coffee_menu = f'''               
                        --------MENU--------
                        Espresso   (E) ${MENU['espresso']['cost']}
                        Latte      (L) ${MENU['latte']['cost']}                                  
                        Cappuccino (C) ${MENU['cappuccino']['cost']}
                        --------------------
'''
machine_income = 0

def coffee_machine_start(): # Displays logo and prompts user to order the coffee
    print(logo)
    print(coffee_menu)
    while True:
        user_choice = get_user_choice()
        if user_choice in MENU:
            order = user_choice
            customer_pay = MENU[order]['cost']
            print(f"You ordered a {order}. It costs ${customer_pay}.")
            return order, customer_pay
        elif user_choice == 'off':
            print("Turning off the machine...\nPower off.")
            return 'off', None
        elif user_choice == 'info':
            print(f"Water: {resources['water']} mL\nMilk: {resources['milk']} mL\nCoffee: {resources['coffee']} g\nMoney: $ {round(machine_income, 2)} USD")
        elif user_choice == 'refill':
            refill_coffee_machine()
        else:
            print("Invalid input. Please try again.")

def refill_coffee_machine():
    print("\n___ Refill Mode ___\n")
    for ingredient in resources:
        try:
            amount = int(input(f"\nHow much {ingredient} would you like to add? "))
            resources[ingredient] += amount
        except ValueError:
            print("Please input a number...")
    print("Refill complete!\n")

def get_user_choice():
    user_choice = input("\nWhat type of coffee would you like?\n").lower()
    if user_choice == 'e':
        return 'espresso'
    elif user_choice == 'l':
        return 'latte'
    elif user_choice == 'c':
        return 'cappuccino'
    elif user_choice == 'off':
        return 'off'
    elif user_choice == 'info':
        return 'info'
    elif user_choice == 'refill':
        return 'refill'

def process_coins():
    print("Please insert coins...\n")
    try:
        quarters = int(input("\nHow many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickles = int(input("How many nickles? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
    except ValueError:
        print("Invalid coin input. Defaulting to $0...")
        return 0.0
    return round((quarters + dimes + nickles + pennies),2)

def is_payment_sufficient(amount_paid, cost):
    if amount_paid < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif amount_paid > cost:
        change = round(amount_paid - cost, 2)
        print(f"Thank you. Here is your change of ${change}.\n")
    else:
        print("Thank you for the exact payment!")
    return True

def is_resource_sufficient(drink_name):
    drink_ingredients = MENU[drink_name]["ingredients"]
    for ingredient, amount_required in drink_ingredients.items():
        if ingredient in resources:
            if resources[ingredient] < amount_required:
                print(f"Sorry, there is not enough {ingredient}. Money refunded.")
                return False
    return True

def make_coffee(drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount



def coffee_machine():
    global machine_income
    machine_running = True

    while machine_running:
        user_order, coffee_price = coffee_machine_start()

        if user_order == 'off':
            print("Turning off the machine...\nPower off.")
            machine_running = False
            break

        if user_order in MENU:
            amount_paid = process_coins()
            print(f"You paid ${amount_paid}.\n")

            if is_resource_sufficient(user_order):
                if is_payment_sufficient(amount_paid,coffee_price):
                    machine_income += coffee_price
                    make_coffee(user_order)
                    print(f"Enjoy your {user_order}!\n{coffee_mug}\n")
                    continue

coffee_machine()