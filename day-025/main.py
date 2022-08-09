import pandas
import turtle
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("The U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
data = pandas.read_csv("50_states.csv")
score = 0
correct_guesses = []


while game_is_on:

    if score < 1:
        the_title = "Guess the State"
    else:
        the_title = f"{score}/50 States Correct"

    answer_state = screen.textinput(title=the_title, prompt="Type another state's name").title()
    # If player's answer is in the list of states
    for state in data["state"]:
        if answer_state == state:
            score += 1
            correct_guesses.append(answer_state)

            # Get name and location of the state
            this_row = data[data.state == answer_state]
            new_x = int(this_row["x"])
            new_y = int(this_row["y"])

            # Create a turtle to draw the name in the correct location
            new_turtle = StateWriter(x=new_x, y=new_y, name=answer_state)

    if score == 50:
        game_is_on = False


turtle.mainloop()
