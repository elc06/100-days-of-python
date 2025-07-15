#Game design to-do list
# 1. Create a game logo to display at start
# 2. Show a welcome message and game instructions
# 3. Allow player to choose difficulty (Easy = 10 tries, Hard = 5 tries)
# 4. Generate a random number between 1 and 100
# 5. Prompt the user to guess the number
# 6. Validate user input (number within range and valid integer)
# 7. Provide feedback (too high, too low, or correct)
# 8. Track and update number of attempts left
# 9. End game when user guesses correctly or runs out of attempts
# 10. Offer to play again or quit

import random

### Game Interface ###
logo = '''
     ▗▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖ ▗▄▄▖     ▗▄▖     ▗▖  ▗▖▗▖ ▗▖▗▖  ▗▖▗▄▄▖ ▗▄▄▄▖▗▄▄▖     
    ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌       ▐▌ ▐▌    ▐▛▚▖▐▌▐▌ ▐▌▐▛▚▞▜▌▐▌ ▐▌▐▌   ▐▌ ▐▌    
    ▐▌▝▜▌▐▌ ▐▌▐▛▀▀▘ ▝▀▚▖ ▝▀▚▖    ▐▛▀▜▌    ▐▌ ▝▜▌▐▌ ▐▌▐▌  ▐▌▐▛▀▚▖▐▛▀▀▘▐▛▀▚▖    
    ▝▚▄▞▘▝▚▄▞▘▐▙▄▄▖▗▄▄▞▘▗▄▄▞▘    ▐▌ ▐▌    ▐▌  ▐▌▝▚▄▞▘▐▌  ▐▌▐▙▄▞▘▐▙▄▄▖▐▌ ▐▌    
                                                                                                                                                           
'''
win = """
▄▖          ▗   ▌
▌ ▛▌▛▌▛▌▛▘▀▌▜▘▛▘▌
▙▖▙▌▌▌▙▌▌ █▌▐▖▄▌▖
      ▄▌         
"""


easy_level = 10
hard_level = 5

def game_difficulty():
    while True:
        level = input("Choose a difficulty for 'Easy' or 'Hard'?\n").lower()
        if level == "easy":
            return easy_level
        elif level == "hard":
            return hard_level
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def num_checking(user_guess, number):
    if user_guess > number:
        print("Too high.")
        return False
    elif user_guess < number:
        print("Too low.")
        return False
    elif user_guess == number:
        print(win)
        return True

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    game_attempts = game_difficulty()

    while game_attempts > 0:
        print(f"You have {game_attempts} attempts remaining.")
        try:
            user_guess_num = int(input("Make a guess: "))
        except ValueError:
            print("Invalid, please try again.")
            continue
        if user_guess_num < 1 or user_guess_num > 100:
            print("Choose a number between 1 and 100.")
            continue

        if num_checking(user_guess_num, number):
            break
        else:
            game_attempts -=1

        if game_attempts == 0:
            print(f"Game over. The number was {number}.")


def game_play():
    while True:
        game()
        replay = input("Do you want to play again? 'yes' or 'no'?\n").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break

game_play()