#day6 was made in a site

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif not front_is_clear():
        turn_left()
        if not front_is_clear():
            turn_left()
    move()
