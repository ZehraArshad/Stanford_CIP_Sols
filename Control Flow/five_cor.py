    for i in range(5):
        putting()


def putting():
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
    turn_right()

    
def turn_right():
    turn_left()
    turn_left()
    turn_left()