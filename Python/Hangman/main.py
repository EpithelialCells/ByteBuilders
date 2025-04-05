'''
Import relevant modules
'''
import random # module that enables random selection
import ui # custom-made module (ui.py)
import os # module that controls command line interface

'''
Pregame
'''
right_guesses = [] # List to store correct guesses
wrong_guesses = [] # List to store wrong guesses

'''
Function to hide unknown letters
'''
def hidden_word(word):
    output = ''
    for letter in word:
        if letter in right_guesses:
            output += letter.upper()
        else:
            output += '_'
        output += ' '
    return output

with open('words.txt', 'r') as file:
    word_list = file.read().split('\n')
word = random.choice(word_list)
lives = 6

while lives != 0:
    ui.main_screen(hidden_word(word), wrong_guesses, lives)
    print(ui.print_hangman(6 - lives))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha():
        print("Please enter a LETTER!")
    elif len(guess) != 1:
        print("Please enter ONE letter!")
    elif guess in right_guesses or guess in wrong_guesses:
        print("This letter has been guessed before!")
    else:
        if guess in word:
            right_guesses.append(guess)
        else:
            wrong_guesses.append(guess)
            lives -= 1

    if all(letter in right_guesses for letter in word):
        os.system('cls')
        print(f"Congratulations! You've guessed the word: {word.upper()}!")
        break

if lives == 0:
    print("You ran out of lives :( The word was:", word.upper())
    print(ui.print_hangman(6 - lives))
