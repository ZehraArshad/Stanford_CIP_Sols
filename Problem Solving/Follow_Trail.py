def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while beepers_present():
        follow_straight_trail()
        step_backwards()

        turn_left()
        move()
        if no_beepers_present():

            step_backwards()
            turn_around()
            move()

def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()

def step_backwards():
    """
    Turn around and go back one step, 
    then face the same way you were when you started
    """
    turn_around()
    move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()



def pick():
    while beepers_present():
        pick_beeper()
        move()

