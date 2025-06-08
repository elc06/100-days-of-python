import random

rock = '''Rock
   _______
---'   ____)
     (_____)
     (_____)
     (____)
---.__(___)
'''

paper = '''Paper
   _______
---'   ____)____
         ______)
         _______)
        _______)
---.__________)
'''

scissors = '''Scissors
   _______
---'   ____)____
         ______)
      __________)
     (____)
---.__(___)
'''

game_choices = [rock, paper, scissors]

###User Input
user_input = input("What is your choice?\n 0 for Rock, 1 for Paper, 2 for Scissors:\n")

if user_input not in ["0", "1", "2"]:
   print("Invalid input! You must choose 0, 1, or 2.")
else:
   user_choice = int(user_input)
   print(f"\nYou chose:\n{game_choices[user_choice]}")

   ###Bot
   bot_choice = random.randint(0, 2)
   print(f"Bot chose:\n{game_choices[bot_choice]}")

   ###Game Rule
   if user_choice == bot_choice:
       print("It's a draw!")
   elif (user_choice == 0 and bot_choice == 2) or \
        (user_choice == 1 and bot_choice == 0) or \
        (user_choice == 2 and bot_choice == 1):
       print("You win!!!")
   else:
       print("You lose :(")