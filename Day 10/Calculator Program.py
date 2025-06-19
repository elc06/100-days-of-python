logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculator_input():

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    first_num = float(input("What's the first number?\n"))

    con_calculator = True

    while con_calculator:

        operator = input("Pick an operator from the following:\n +\n -\n *\n /\n")
        next_num = float(input("What's the next number?\n"))

        user_operation = operations.get(operator)

        if user_operation:
            result = user_operation(first_num, next_num)
            print(f"{first_num} {operator} {next_num} = {result}")
        else:
            print("Invalid operator.")

        user_choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'stop':\n").lower()
        if user_choice == "y":
            first_num = result
        elif user_choice == "n":
            calculator_input()
            return
        elif user_choice == "stop":
            print("Bye bye!")
            con_calculator = False

calculator_input()