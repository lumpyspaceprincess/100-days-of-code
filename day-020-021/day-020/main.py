import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision detection with food
    if snake.head_of_snake.distance(food) < 15:
        food.respawn()
        scoreboard.increase_score()
        snake.extend()

    # Collision detection with wall
    if snake.head_of_snake.xcor() > 280 or snake.head_of_snake.xcor() < -280 \
            or snake.head_of_snake.ycor() > 280 or snake.head_of_snake.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Collision detection with tail
    for segment in snake.segments[1:]:
        if snake.head_of_snake.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
