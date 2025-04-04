import os

def main_screen(word, wrong_letters, lives):
     os.system('cls')
     print(f"You have {lives} lives left!")
     print(f"Your word is: {word}")
     print(f"Wrong guesses: {wrong_letters}")

def print_hangman(n):
    s = '   _____\n  |     |\n  |     |\n  |     |\n'
    l = ['  |\n  |\n  |\n__|__',
         '  |     0\n  |\n  |\n__|__',
         '  |     0\n  |     |\n  |\n__|__',
         '  |     0\n  |    /|\n  |\n__|__',
         '  |     0\n  |    /|\\\n  |\n__|__',
         '  |     0\n  |    /|\\\n  |    / \n__|__',
         '  |     0\n  |    /|\\\n  |    / \\\n__|__']
    return s+l[n]