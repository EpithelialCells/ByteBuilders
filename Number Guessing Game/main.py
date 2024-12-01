import random


correct_number = random.randint(1,100)

guesses_left = 5
while guesses_left > 0:
    guess = int(input("Guess a number: "))
    if guess == correct_number:
        break
    elif guess < correct_number:
        print("Too small!")
    else:
        print("Too big!")
    guesses_left -= 1

if guesses_left == 0:
    print("Lose!")
else:
    print("Win!")