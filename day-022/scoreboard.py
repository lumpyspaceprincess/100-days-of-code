from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("grey")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score}   |   {self.right_score}", align=ALIGNMENT, font=FONT)

    def game_over(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, 100)
        self.write(f"{winner} wins!", align=ALIGNMENT, font=FONT)
