from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head_of_snake = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(900, 900)
        self.segments.clear()
        self.create_snake()
        self.head_of_snake = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head_of_snake.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_of_snake.heading() != DOWN:
            self.head_of_snake.setheading(UP)

    def right(self):
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)

    def down(self):
        if self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)

    def left(self):
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)
