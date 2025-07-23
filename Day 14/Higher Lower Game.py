# Higher Lower Game - Functional Design
#   1. Display the game logo when the program starts.
#   2. Prompt the player to enter 'Play' to begin the game.
#   3. Randomly select a data item (A) from the database and display its information (name description, and following count.)
#   4. Randomly select a different data item (B) from the database (excluding A). Only show its name and description, but hide its follower count.
#   5. Ask the player to guess whether B has a higher or lower follower count than A.
#   6. If the player's guess is correct:
#       -Increase the score by 1.
#       -Set B as the new A.
#       -Select a new B and repeat from step 4.
#       -Display the updated score each round.
#  7. If the player's guess is incorrect:
#       -End the game.
#       -Display the final score.
#       -Ask if they want to play again.
#       -If yes, restart the game and display the highest score achieved so far.

# Functions needed:
# While loop
# For loop
# if-else statements
# An empty list to store player's highest score

import random
import game_data
import art

def game_start(): # Displays logo and prompts user to start the game by typing 'Play'
    print(art.logo)
    print("-----Welcome to the higher lower game-----")
    while True:
        start = input("Enter 'Play' to begin the game:\n").lower()
        if start == 'play':
            return
        else:
            print("Invalid input, please try again.")

def data_pair(dataset): #Returns a unique pair of data items (A, B) from the dataset
    a = random.choice(game_data.data)
    b = random.choice(game_data.data)
    while a == b:
        b = random.choice(game_data.data)
    return a, b

def check_answer(guess,a_follower_count,b_follower_count): # Returns True if the user's guess matches the correct answer based on follower count
    if a_follower_count > b_follower_count:
        return guess == 'l'
    elif b_follower_count > a_follower_count:
        return guess == 'h'

def update_score(user_score, user_correct): # Increases and returns the score if the user guessed correctly
    if user_correct:
        user_score +=1
    return user_score

def play_again(): # Prompts user to play again; returns True or False
    while True:
        choice = input("Do you want to play again? (y/n)?\n").lower()
        if choice == "y":
            return True
        elif choice == "n":
            print("Bye bye. Thank you for playing!")
            return False
        else:
            print("Invalid input. Please enter ('y' or 'n').")

def game(): # Runs the full game loop including scoring and replay option
    highest_score = 0
    game_start()
    keep_playing = True
    while keep_playing:
        score = 0
        a, b = data_pair(game_data.data)
        game_running = True
        while game_running:
            print(f"{a['name']} is a {a['description']} from {a['country']}, has a follower count of {a['follower_count']} million.")
            print(art.vs)
            print(f"{b['name']} is a {b['description']} from {b['country']}.")
            user_guess = input(f"{b['name']} has a higher or lower follower counts? Enter 'H' for higher, 'L' for lower:\n").lower()
            user_correct = check_answer(guess=user_guess, a_follower_count=a['follower_count'],b_follower_count=b['follower_count'] )
            if user_correct:
                score += 1
                print(f"\nCorrect! {a['name']} has {a['follower_count']}M, and {b['name']} has {b['follower_count']}M.")
                print("\n" + "-" * 50)
                a = b
                b = random.choice(game_data.data)
                while b == a:
                    b = random.choice(game_data.data)
            else:
                print(f"\nWrong :(... {a['name']} has {a['follower_count']}M, and {b['name']} has {b['follower_count']}M.")
                print(f"Your final score is {score}.")
                if score > highest_score:
                    highest_score = score
                    print(f"New high score: {highest_score}!!")
                else:
                    print(f"Highest score: {highest_score}.")
                game_running = False
        keep_playing = play_again()

game()