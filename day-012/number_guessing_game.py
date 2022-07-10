# Day 12 project of 100 Days of Code
# Number guessing game

from art import logo
import random
import os


def create_the_number():
    num = random.choice(range(1, 101))
    return num


def difficulty_test(level):
    if level == "hard":
        return 5
    elif level == "easy":
        return 10
    else:
        print("Invalid choice. For insulting me, level is set to hard.")
        return 5


def valid_number(num):
    if num not in range(1, 101):
        print("Invalid choice, the number is between 1 and 100.")
        return False
    return True


def higher_lower_test(the_guess, the_target):
    if the_guess > the_target:
        return "high"
    else:
        return "low"


def main_loop(turns_remaining, the_target):
    while turns_remaining > 0:
        print(f"You have {turns_remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if valid_number(guess):
            if not guess == the_target:
                print(f"Too {higher_lower_test(guess, the_target)}.")
                turns_remaining -= 1
                if turns_remaining > 0:
                    print("Guess again.")
                else:
                    print("You've run out of guesses, you lose.")
            else:
                print(f"You got it! The answer was {the_target}.")
                turns_remaining = 0


game_running = True

while game_running:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    the_number = create_the_number()
    # print(f"Pssst, the correct answer is {the_number}")  # For debugging
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    difficulty_number = difficulty_test(game_difficulty)
    main_loop(difficulty_number, the_number)
    repeat = input("Would you like to play again? Type 'y' or 'n': ").lower()
    if not repeat == "y":
        game_running = False
