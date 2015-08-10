#!/usr/bin/env python
# HW05_ex00_TextAdventure.py

#TextAdventure update requirements: 

# 1. Get the game to run
# 2. Change the name of the function from start() to main()
# 3. Personalize the game. Take the username from the command line and update 
#    each function where it says "you", it should print the username.
# 4. In bear_room, make it so that user can enter "take" or "honey", and just 
#    "taunt", and open" or "door"
# 5. infinite_stair_room is not connected to anything, connect it

# Extra nerd credit
# Create a new room back_room, which the player enters through a 'back' door.
# Describe that it's filled with awkward programmers. You state your name but nobod listens.
# You soon start programming python and never leave. exit(0) the game.



##############################################################################
# Imports
import sys

# Body


def infinite_stairway_room(name, count=0):
    print "You walk through the door to see a dimly lit hallway.".replace("You ", " "+name+" ")
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'.replace(" you ", " "+name+" ")
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print 'You take the stairs'.replace(" you ", " "+name+" ")
        if (count > 0):
            print "but you're not happy about it"
            infinite_stairway_room(name, count + 1)

    if next == "leave room":
        bear_room(name)


def gold_room(name):
    print "This room is full of gold.  How much do you take?".replace(" you ", " "+name+" ")

    next = raw_input("> ")
    try :
        how_much = int(next)
    except Exception:
        dead("Man, learn to type a number.",name)

    if how_much < 50:
        print "Nice, you're not greedy, you win!".replace(" you ", " "+name+" ")
        exit(0)
    else:
        dead("You greedy bastard!",name)


def bear_room(name):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "There is a door on the right with no bear protecting it"
    print "What are you going to do?".replace(" you ", " "+name+" ")
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at you then slaps your face off.",name)
        elif (next == "taunt" or next == "bear") and not bear_moved:
            print "The bear has moved from the door. You can go through it now.".replace(" You ", " "+name+" ")
            bear_moved = True
        elif (next == "taunt" or next == "bear") and bear_moved:
            dead("The bear gets pissed off and chews your leg off.",name)
        elif (next == "open" or next == "door") and bear_moved:
            gold_room(name)
        
        elif next == "take right door":
            infinite_stairway_room("ankur",2)

        else:
            print "I got no idea what that means."


def cthulhu_room(name):
    print "Here you see the great evil Cthulhu.".replace(" you ", " "+name+" ")
    print "He, it, whatever stares at you and you go insane.".replace(" you ", " "+name+" ")
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!",name)
    else:
        cthulhu_room(name)


def dead(why, name):
    print why, 
    print "You are dead !".replace("You ", " "+name+" ")
    exit(0)


def back_room(name):
    print "You are in the back room.".replace("You",name)
    print ("This room is filled with awkward programmers")
    print ("You state your name but nobody listens")
    print ("You soon start programming python and never leave")

    while (True):
        usrInput = raw_input("> ")

        if(usrInput == "exit(0)"):
            break



##############################################################################
def main():
    # START the TextAdventure game

    name = sys.argv[1]

    print "You are in a dark room.".replace(" you ", " "+name+" ")
    print "There is a door to your right and left."
    print "Which one do you take?".replace(" you ", " "+name+" ")

    next = raw_input("> ")

    if next == "left":
        bear_room(name)
    elif next == "right":
        cthulhu_room(name)
    
    elif next == "back":
        back_room(name)

    else:
        dead("You stumble around the room until you starve.").replace(" you ", " "+name+" ")

if __name__ == '__main__':
    main()
