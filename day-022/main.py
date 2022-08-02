from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((369, 0))

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
ball = Ball()
scoreboard = Scoreboard()

MAX_SCORE = 2
game_is_on = True

while game_is_on:
    screen.update()

    # Detect collision with right paddle
    if ball.xcor() >= 360:
        if ball.distance(right_paddle) < 50:
            ball.x_direction = "west"
            ball.speed_up()
        # Detect when right paddle misses
        else:
            ball.respawn()
            ball.ball_speed = 3
            scoreboard.left_score += 1
            if scoreboard.left_score == MAX_SCORE:
                scoreboard.game_over("Left")
                game_is_on = False
            else:
                scoreboard.refresh_scoreboard()

    # Detect collision with left paddle
    if ball.xcor() <= -360:
        if ball.distance(left_paddle) < 50:
            ball.x_direction = "east"
            ball.speed_up()
        # Detect when left paddle misses
        else:
            ball.respawn()
            ball.ball_speed = 3
            scoreboard.right_score += 1
            if scoreboard.right_score == MAX_SCORE:
                scoreboard.game_over("Right")
                game_is_on = False
            else:
                scoreboard.refresh_scoreboard()

    # Detect collision with walls
    if ball.ycor() >= 290:
        ball.y_direction = "south"

    if ball.ycor() <= -280:
        ball.y_direction = "north"

    ball.move()

screen.exitonclick()
