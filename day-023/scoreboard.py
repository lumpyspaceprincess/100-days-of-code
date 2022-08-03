from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")
FONT_LARGER = ("Courier", 42, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 1
        self.color("grey")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.player_score}", align=ALIGNMENT, font=FONT)

    def game_over(self, level):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT_LARGER)
