

from karel.stanfordkarel import *

def main():
    move()
    if beepers_present():
        pick_beeper()
        turn_left()
        while front_is_clear():
            move()
        turn_left()
        turn_left()
        turn_left()
    put_beeper()
    move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()