import turtle
from turtle import Turtle, Screen
import random
from hirst import colour_extractor

timmy = Turtle()
timmy.shape("circle")
timmy.hideturtle()
timmy.speed("fastest")
timmy.width(1)
turtle.colormode(255)


def colour_randomiser():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return r, g, b


#  Draw a series of shapes with increasing numbers of sides:
#
# for num_of_sides in range(3, 100):
#     colour_randomiser()
#     count = num_of_sides
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy.forward(10)
#         timmy.right(angle)
#         count -= 1


# Draw a random walk in random colours
#
# for _ in range(1000):
#     timmy.color(colour_randomiser())
#     my_list = [0, 90, 180, 270]
#     choice = float(random.choice(my_list))
#     timmy.setheading(choice)
#     timmy.forward(15)


# Draw a spirograph
# def draw_spirograph(size_of_gap):
#     for angle in range(size_of_gap):
#         timmy.color(colour_randomiser())
#         timmy.setheading(angle * (360 / size_of_gap))
#         timmy.circle(100)
#
# draw_spirograph(40)


# Draw a painting
def draw_hirst_painting():
    hirst_list = colour_extractor("image.jpg")
    grid_size = 10
    grid_sparseness = 50
    timmy.penup()
    timmy.setposition(-500, -300)

    def draw_line_of_dots():
        for _ in range(grid_size):
            timmy.color(random.choice(hirst_list))
            timmy.forward(grid_sparseness)
            timmy.stamp()

    def move_up_a_row():
        timmy.left(90)
        timmy.forward(grid_sparseness)
        timmy.right(90)
        timmy.backward(grid_sparseness * grid_size)

    rows_left = grid_size

    while rows_left > 0:
        draw_line_of_dots()
        rows_left -= 1
        if rows_left > 0:
            move_up_a_row()

draw_hirst_painting()

screen = Screen()
screen.exitonclick()
