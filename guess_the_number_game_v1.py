# Implementation for "Guess the number" mini-project v1.0
# input will come from buttons and an input field
# all output for the game will be printed in the console
# This code is only valid in codeskulptor

import random
import simplegui
# My global variables
secret_number = counter = 0
num_range = 100
low = 0
num_of_guess = 7

# helper function to start and restart the game
def new_game():
    global counter, secret_number, num_range, low
    counter = 0
    secret_number = random.randrange(0,num_range)   
    print "\nStarting a new game. Range is ",low, "--", num_range
    
# define event handlers for control panel
def range100():
    # Button for the 100 range guess game
    global num_range, num_of_guess
    num_range = 100
    num_of_guess = 7
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global secret_number, num_of_guess, num_range
    num_range = 1000
    num_of_guess = 10
    secret_number = random.randrange(0,num_range)
    new_game()
    
def input_guess(guess):
    global secret_number, counter, num_of_guess
    
    # Catch errors casued by non-integer inputs
    try:
        guess = int(guess)
    except:
        print "Please Enter only Integers. Thank you\n"
        return
    
    # If input is integer, continue the execution
    counter += 1  #increment counter
    if (counter) < num_of_guess:
        print "The guess was: ", guess
        if guess > secret_number:
            print "Lower"
            print "You have ", num_of_guess - counter, " guesses remaing\n"
        elif guess < secret_number:
            print "Higher"
            print "You have ", num_of_guess - counter, " guesses remaing\n"
        else:
            print "Correct"
            new_game()
    elif (counter) == num_of_guess:
        print "The guess was ", guess
        if guess > secret_number:
            print "Lower"
            print "You have exhausted your chances.\n\n"
            new_game()
        elif guess < secret_number:
            print "Higher"
            print "You have exhausted your chances.\n\n"
            new_game()
        else:
            print "Correct"
            new_game()
    
# create frame
frame = simplegui.create_frame("Guess the Number game",400,400)

# register event handlers for control elements and start frame
button1 = frame.add_button("Range 100", range100, 100)
button2 = frame.add_button("Range 1000", range1000, 100)
inp = frame.add_input("Input Label", input_guess, 100)

# call new_game 
new_game()