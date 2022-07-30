from turtle import Screen, Turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
number_of_turtles = 6
bale_of_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which colour turtle will win the race? ")


def esio_setup(num):
    i = 0
    pos_x = -230
    pos_y = -125
    while i < num:
        bale_of_turtles[i].penup()
        bale_of_turtles[i].color(colours[i])
        bale_of_turtles[i].goto(pos_x, pos_y)
        i += 1
        pos_y += 50


def esio_creator(num):
    for turtle_index in range(0, num):
        esio = Turtle(shape="turtle")
        bale_of_turtles.append(esio)
    esio_setup(num)


esio_creator(number_of_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in bale_of_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You win!")
            else:
                print("You lose!")
            print(f"The winning colour was {winning_colour}.")


screen.exitonclick()
