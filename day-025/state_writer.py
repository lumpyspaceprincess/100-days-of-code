from turtle import Turtle

FONT = ('Courier', 14, 'normal')

class StateWriter(Turtle):

    def __init__(self, x, y, name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x, y)
        self.write(name, font=FONT)
