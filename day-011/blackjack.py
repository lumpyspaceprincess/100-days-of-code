# Day 11 of 100 Days of Code
# Blackjack game

import random
from art import logo
import os


def bust_check(hand):
    bust = False
    if sum(hand) > 21:
        if 11 in hand:   # if ACE in hand and sum over 21, set ACE to worth 1
            position = hand.index(11)
            hand[position] = 1
        else:
            bust = True
    return bust


def dealers_game():     # Dealer can play their entire game in one go, as it
    user = []           # won't be revealed to the user until the end anyway
    while sum(user) <= 16:
        user.append(random.choice(cards))
        bust_check(user)
        if len(user) == 2:
            if blackjack_detected([0], user):
                game_continue()
    return user


def dealing(num_of_cards, user):
    for i in range(num_of_cards):
        user.append(random.choice(cards))
    return user


def score(user):
    return sum(user)


def five_card_charlie(human, robot):
    if len(human) == 5 or len(robot) == 5:
        has_it_happened = True
        if len(human) == 5:
            return has_it_happened, "You", human, "You"
        else:
            return has_it_happened, "The Dealer", robot, "They"
    else:
        has_it_happened = False
        return has_it_happened, "", human, ""
    

def final_scores(player, dealer):
    sum_player = score(player)
    sum_dealer = score(dealer)
    five_card_achieved, five_card_holder, holder_hand, pronoun = five_card_charlie(player, dealer)
    if sum_dealer > 21:
        print(f"The dealer went bust, scoring {sum_dealer} with the hand {dealer}. You win!")
    elif five_card_achieved:
        print(f"{five_card_holder} achieved a Five Card Charlie with the hand {holder_hand}. {pronoun} win!")
    elif sum_player == sum_dealer:
        print(f"The dealer scored {sum_dealer} with the hand {dealer}."
              f"You scored {sum_player} with the hand {player}. The game is a draw.")
    elif sum_player > sum_dealer:
        print(f"Your score of {sum_player} beat the dealer's score of {sum_dealer}. You win!")
    else:
        print(f"The dealer's score of {sum_dealer} beat your score of {sum_player}. You lose.")


def dealing_loop(player_hand, dealer_hand):
    continuing = True
    while continuing:
        should_continue = input(f"Type 'y' to twist, type 'n' to stick: ").lower()
        if should_continue == "y":
            dealing(1, player_hand)
            bust = bust_check(player_hand)
            if bust:
                print(f"You went bust with a score of {score(player_hand)}, you lose.")
                continuing = False
            else:
                print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        else:
            continuing = False
    if not score(player_hand) > 21:
        final_scores(player_hand, dealer_hand)


def blackjack_detected(human, robot):
    if score(human) == 21:
        print(f"BLACKJACK! You win!")
        return True
    if score(robot) == 21:
        print(f"The dealer has BLACKJACK with the cards {robot}. You lose.")
        return True
    return False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game_continue():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    player_hand = dealing(2, [])
    print(f"Your cards are {player_hand}, current score {score(player_hand)}")
    dealer_hand = dealers_game()
    print(f"Dealer's first card is {dealer_hand[0]}")

    if not blackjack_detected(player_hand, []):
        dealing_loop(player_hand, dealer_hand)

    var = input("Would you like to play again? Enter 'y' or 'n': ").lower()
    if var == "y":
        game_continue()


game_continue()
