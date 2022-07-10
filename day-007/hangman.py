import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6
already_guessed = []

# Testing code
# print(f"HINT, the solution is {chosen_word}.")

# Create blanks
display = []
for letter in chosen_word:
    display += "_"

print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    # Check if guess has been made previously
    if guess not in already_guessed:
        already_guessed += guess

        # Check guessed letter
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

        # Join the list and turn it into a string.

        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print(f"The letter '{guess} is not in this word")
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
    else:
        print("You have already tried this letter.")
