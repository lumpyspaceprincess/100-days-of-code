import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo", "C": "Charlie"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
my_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.


def nato_alphabetiser():
    user_input = input("Type a word: ").upper()

    try:
        output_list = [my_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        nato_alphabetiser()
    else:
        print(output_list)


nato_alphabetiser()
