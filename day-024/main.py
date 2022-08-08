PLACEHOLDER = "[name]"

# Get a list of names
names_list = []
with open("./Input/Names/invited_names.txt", mode="r") as data:
    my_list = data.readlines()

    # Remove newlines from list
    for name in my_list:
        names_list.append(name.strip("\n"))

# For each name in the list of names
for name in names_list:

    # Open the sample letter
    with open("./Input/Letters/starting_letter.txt", mode="r") as data:
        letter = data.read()

        # 2. Replace the [name] placeholder with the actual name.
        new_letter = letter.replace(PLACEHOLDER, name)

        # 3. Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{name}", "w") as file:
            file.write(new_letter)
