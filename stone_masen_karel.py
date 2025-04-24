from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    up()
    to_next_col()
    down()
    to_next_col()
    up()
    to_next_col()
    down()
    
    
def to_next_col():
    for i in range(4):
        move()
    
def up():
    turn_left()
    put_beepers()
    turn_around()

def down():
    turn_around()
    put_beepers()
    turn_left()

def put_beepers():
    while front_is_clear():
        put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

def turn_around():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()