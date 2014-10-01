# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number = 0
number_of_guesses = 7
number_range = 100

# helper function to start and restart the game
def new_game(number_range):
    # initialize global variables used in your code here
    global secret_number
    global number_of_guesses
   
    if number_range == 100:
        number_of_guesses = 7
    elif number_range == 1000:
        number_of_guesses = 10
   
    secret_number = random.randrange(0, number_range)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_range
    number_range = 100
    new_game(number_range)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number_range
    number_range = 1000
    new_game(number_range)
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global number_of_guesses
    
    print 'Guess was ' + guess
    guess_int = int(guess)
    number_of_guesses -= 1
    print number_of_guesses
    
    if number_of_guesses != 0:
        if guess_int > secret_number:
            print 'Lower'
        elif guess_int < secret_number:
            print 'Higher'
        elif guess_int == secret_number:
            print 'Correct'
            new_game(number_range)
    else:
        print 'Too many guesses.'
        new_game(number_range)
        
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button('Range: 0 - 100', range100)
frame.add_button('Range: 0 - 1000', range1000)
frame.add_input('Guess', input_guess, 50)

# call new_game 
new_game(number_range)
frame.start()

# always remember to check your completed program against the grading rubric
