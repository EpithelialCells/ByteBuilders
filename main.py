'''
Import relevant modules
'''
import random # module that enables random selection

'''
Pregame
'''
correct_number = random.randint(1,100) # pick a random number from 1-100
guesses_left = 5 # store guesses left as a variable

'''
Game loop
'''
while guesses_left > 0: # repeats as long as player has enough guesses
    guess = int(input("Guess a number: ")) # take player input
    if guess == correct_number:
        break # break out of loop if correct guess
    elif guess < correct_number:
        print("Too small!")
    else:
        print("Too big!")
    guesses_left -= 1

'''
Endgame
'''
if guesses_left == 0:
    print("Lose!")
else:
    print("Win!")