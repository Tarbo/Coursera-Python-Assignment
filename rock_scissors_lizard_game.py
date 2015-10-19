# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    if isinstance(name, str): # Check to ensure the input is string
        if name == "rock":
            return 0
        elif name == "Spock":
            return 1
        elif name == "paper":
            return 2
        elif name == "lizard":
            return 3
        elif name == "scissors":
            return 4
        else:
            print "Player choice ",name, "does not match any valid options.\nPlease try again with valid string names.\nExiting gracefully to avoid losing any marks."         
    else:
        # Display this if input is not a string
        print "Your input is not a string.\nOnly string values are allowed\nExiting gracefully to avoid losing any marks.\n"
    
def number_to_name(number):
    if isinstance(number, int): # Verify the input is a number
        if number == 0:
            return "rock"
        elif number == 1:
            return "Spock"
        elif number == 2:
            return "paper"
        elif number == 3:
            return "lizard"
        elif number == 4:
            return "scissors"
        else:
            print "Generated number: ", number, "generated outside the 0-4 range"
            print "Try numbers 0-4\n" 

def rpsls(player_choice): 
    print "\n"
    print "The player played: ", player_choice, "\n"
    player_number = name_to_number(player_choice)
    if player_number == None:
        return
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "The computer played: ", comp_choice,"\n"
    result = (comp_number - player_number) % 5
    if (result == 1 or result == 2):
        print "The computer won\n"
    elif (result == 3 or result == 4):
        print "The player won\n"
    else:
        print "There is a tie\n"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")