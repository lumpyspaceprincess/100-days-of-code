from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("lime")
        self.respawn()
        self.x_direction = "east"
        self.y_direction = "north"
        self.ball_speed = 3

    def respawn(self):
        self.goto(0, -280)

    def move(self):
        if self.x_direction == "east":
            new_x = self.xcor() + self.ball_speed
        elif self.x_direction == "west":
            new_x = self.xcor() - self.ball_speed

        if self.y_direction == "north":
            new_y = self.ycor() + self.ball_speed
        elif self.y_direction == "south":
            new_y = self.ycor() - self.ball_speed

        self.goto(new_x, new_y)

    def speed_up(self):
        self.ball_speed += 0.5
