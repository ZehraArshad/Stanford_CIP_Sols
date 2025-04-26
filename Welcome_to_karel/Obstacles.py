"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move()
    for i in range(3):
        beeper()
    while front_is_clear():
        move()


def beeper():
    up()
    right()
    place_beeper() 

def right():
    turn_around()
    move()
    

    
def up():    
    turn_left()
    while front_is_clear():
        move()



def turn_around():
    turn_left()
    turn_left()
    turn_left()

def place_beeper():
    turn_around()
    while front_is_clear():
        move()
    put_beeper()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()