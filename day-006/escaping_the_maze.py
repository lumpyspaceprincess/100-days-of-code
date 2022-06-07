# Solution to Reeborg's World Maze problem at reeborg.ca
# Functions refer to in-game functions


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def moving():
    if front_is_clear():
        if not at_goal():
            move()


def left_is_clear():
    turn_left()
    if front_is_clear():
        turn_right()
        return True
    else:
        turn_right()
        return False


while not at_goal():
    if not right_is_clear():
        if front_is_clear():
            move()
            if right_is_clear():
                turn_right()
                moving()
                turn_right()
        else:
            turn_left()
    elif front_is_clear():
        move()
    else:
        turn_left()
