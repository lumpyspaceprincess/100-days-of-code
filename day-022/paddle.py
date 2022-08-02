from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color("white")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y > 270:
            new_y = 270
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y < -270:
            new_y = -270
        self.goto(self.xcor(), new_y)
