import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

rps_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number, you lose.")
    quit()

computer_choice = random.randint(0, 2)


def winner(x, y):
    if x == y:
        return "draw"
    elif x == 0 and y == 1:
        return "lose"
    elif x == 1 and y == 2:
        return "lose"
    elif x == 2 and y == 0:
        return "lose"
    else:
        return "win"


print(f"You chose: \n {rps_images[user_choice]}")
print(f"Computer chose: \n {rps_images[computer_choice]}")
print(f"You {winner(user_choice, computer_choice)}.")
