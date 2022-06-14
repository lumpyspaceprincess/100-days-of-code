# Day 008 of 100 Days of Code
# Creating a Caesar cipher

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

cipher_running = True


def caesar(the_text, the_shift, the_direction):
    if the_direction == "encode" or the_direction == "decode":
        processed_message = ""
        for letter in the_text:
            if letter not in alphabet:
                processed_message += letter
            else:
                index = alphabet.index(letter)  # index position of letter in list
                if the_direction == "encode":
                    new_position = index + the_shift
                else:
                    new_position = index - the_shift
                while new_position not in range(0, len(alphabet)):
                    if new_position > 25:
                        new_position -= 26
                    if new_position < 0:
                        new_position += 26
                processed_message += alphabet[new_position]
        print(f"The {the_direction}d text is {processed_message}")
    else:
        print("ERROR: You did not specify encode or decode.")


print(logo)

while cipher_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(the_text=text, the_shift=shift, the_direction=direction)

    restart = input("Do you want to go again? Type Yes or No.\n").lower()
    print(restart)
    if restart == "no":
        print("Ending the programme.")
        cipher_running = False
    elif restart != "yes" and restart != "no":
        print("Invalid selection, ending the programme.")
        cipher_running = False
