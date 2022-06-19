# Day 9 of 100 Days of Code

from art import logo


def clear():
    return "\x1B[2J"


auction_dict = {
    "James": 123,
    "Tom": 145
}

getting_participants = True
print(logo)


def find_winner(bidding_dict):
    current_highest = 0
    name_highest = ""
    for person in bidding_dict:
        bid_amount = bidding_dict[person]
        if bid_amount > current_highest:
            current_highest = bid_amount
            name_highest = person
    print(f"The winner of the auction is {name_highest} who must pay £{current_highest}")


while getting_participants:
    name = input("Enter your name: \n")
    max_bid = int(input("Enter your maximum bid: £"))
    auction_dict[name] = max_bid
    continuing = input("Are there other users to input bids? Enter 'Yes' or 'No': ").lower()
    if continuing == "no":
        getting_participants = False
        find_winner(auction_dict)
    if continuing == "yes":
        print(clear())
