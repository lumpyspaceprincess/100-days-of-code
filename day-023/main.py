import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road_markings import RoadMarkings

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
artist = RoadMarkings()
all_the_cars = []
creation_interval = 1
spawn_chance = 13

screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Detect collision with cars
    for car in all_the_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over(scoreboard.player_score)

    # Detect reaching the other side of the road
    if player.ycor() > 250:
        player.respawn()
        spawn_chance -= 1  # As the game speeds up, cars will spawn more often
        scoreboard.player_score += 1
        scoreboard.refresh_scoreboard()
        for car in all_the_cars:
            car.cars_move_faster()

    # Randomly create new cars
    if creation_interval % spawn_chance == 0:
        new_car = CarManager(scoreboard.player_score)
        all_the_cars.append(new_car)

    for car in all_the_cars:
        car.car_moving()  # Make the cars move forward
        if car.ycor() < -350:  # Remove cars which have left the screen
            all_the_cars.remove(car)

    creation_interval += 1


screen.exitonclick()