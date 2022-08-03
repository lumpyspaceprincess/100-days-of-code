from turtle import Turtle

class RoadMarkings(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(300, 250)
        self.pencolor("black")
        self.pensize(5)
        self.pendown()
        self.setheading(180)
        self.hideturtle()
        self.forward(600)
        self.penup()
        self.goto(300, -250)
        self.pendown()
        self.forward(600)
