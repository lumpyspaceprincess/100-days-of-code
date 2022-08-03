from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSSIBLE_LANES = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self, level):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE + ((level - 1) * MOVE_INCREMENT)
        self.penup()
        self.goto(200, random.choice(POSSIBLE_LANES))
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1.8)


    def car_moving(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())

    def cars_move_faster(self):
        self.move_distance += MOVE_INCREMENT
