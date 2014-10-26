# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game(rng):
    global secret_number, guesses, game_range
    game_range = rng
    if rng == 1000:
        secret_number = random.randrange(0, 1000)
        decrement(12)
        print "New game. Range is from 0 to 1000"
        print ""
    else:
        secret_number = random.randrange(0, 100)
        decrement(9)
        print "New game. Range is from 0 to 100"
        print ""

#helper function to decrement number of guesses
def decrement(num):
    global guesses
    guesses = num
    guesses -= 1
    return guesses

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    new_game(100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    new_game(1000)

def input_guess(guess):
    # main game logic goes here
    converted_guess = int(guess)
    print "Guess was " + guess
    if converted_guess > secret_number:
        decrement(guesses)
        print "Lower"
        print "Number of remaining guesses is " + str(guesses)
        print ""
    elif converted_guess < secret_number:
        decrement(guesses)
        print "Higher"
        print "Number of remaining guesses is " + str(guesses)
        print ""
    else:
        print "Correct"
        print ""
        new_game(game_range)
    win_state()

#helper function to calculate the winning state
def win_state():
    if guesses == 0:
        print "You ran out of guesses. The number was " + str(secret_number)
        print ""
        new_game(game_range)

# create frame

frame = simplegui.create_frame('Guess the number', 100, 170)
inp = frame.add_input('Your guess:', input_guess, 70)
label = frame.add_label('Choose one of these ranges:')
button100 = frame.add_button('Range: 0 - 100', range100)
button1000 = frame.add_button('Range: 0 - 1000', range1000)
frame.start()

# call new_game

new_game(100)