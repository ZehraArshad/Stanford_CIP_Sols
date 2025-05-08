
def main():
    while front_is_clear():

        move()
        spread()
        reset()
        turn_left()
        if front_is_clear():
            move()
            turn_around()
            turn_left()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
        

def spread():
    
    while beepers_present():

        pick_beeper()
        
        if beepers_present():
            while beepers_present():
                move()
            put_beeper()
            turn_around()
            while front_is_clear():
                move()
            turn_around()
            move()
    put_beeper()
    


def reset():
    turn_around()
    move()
    turn_around()
    
def turn_around():
    turn_left()
    turn_left()

