from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highest_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.refresh_scoreboard()

    def get_highest_score(self):
        with open("data.txt", mode="r") as file:
            score = file.read()
            if score:
                return int(score)
            else:
                return 0

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

    def save_highest_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.highscore))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highest_score()
        self.score = 0
        self.refresh_scoreboard()
