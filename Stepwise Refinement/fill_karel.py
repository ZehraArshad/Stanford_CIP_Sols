def main():
    while left_is_clear():
        fill()
    fill()
    while front_is_clear():
        move()


def fill():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()
    turn_left()
    if front_is_clear():
        move()
    turn_left()
    turn_left()
    turn_left()

