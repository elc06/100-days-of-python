import random
import hangman_words
import hangman_art

lives = 6 #user's live

user_name = input("What is your name?\n")
print(f"Hello {user_name}, welcome to...")
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"~~~~~~~~~~~~~~~You have {lives} out of 6 LIVES left~~~~~~~~~~~~~~~")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"\nYou have already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            guessed_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            guessed_letters.append(guess)
            display += "_"


    print("\nWord to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\nGame over......\nThe correct word is {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("!!!!!!!!!!!!!!!!!!!!!!YOU WIN!!!!!!!!!!!!!!!!!!!!!!")

    print(hangman_art.stages[lives])