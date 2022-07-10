# Day 14 of 100 Days of Code
# Higher - Lower game

from art import logo, vs
from game_data import data
import random
import os


def random_account():
    return random.choice(data)


def readability(entry):
    name = entry['name']
    job = entry['description']
    location = entry['country']
    return f"{name}, a {job} from {location}."


def checking_the_answer(player_guess, a, b):
    if a > b:
        if player_guess == "a":
            return True
        else:
            return False
    if b > a:
        if player_guess == "b":
            return True
        else:
            return False


def game_loop():
    account_a = random_account()
    print(logo)
    player_score = 0
    game_continuing = True
    while game_continuing:
        account_b = random_account()
        while account_a == account_b:
            account_b = random_account()
        print(f"Compare A: {readability(account_a)}")
        print(vs)
        print(f"Against B: {readability(account_b)}")
        guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        player_correct = checking_the_answer(guess, a_followers, b_followers)
        print(player_correct)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        if player_correct:
            player_score += 1
            print(f"You're right! Current score: {player_score}.")
            account_a = account_b
        else:
            print(f"Sorry that's wrong. Final score: {player_score}.")
            game_continuing = False


game_loop()
