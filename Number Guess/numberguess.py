'''The task is to create a script that generates a random number between a fixed range, and  if the user guesses the number right in three chances, then user wins otherwise user lose.'''

# Path: Number Guess/numberguess.py

import random

def number_guess():
    # initialize score
    score = 0
    # generate a random number
    number = random.randint(1, 10)
    # take input from the user
    guess = int(input("Guess the number between 1 and 10: "))
    # check if the user guessed the number
    for i in range (1,4,1):
        if guess == number:
            score = score + 1
            print ("You guessed the number right!")
        else:
            print("You guessed the number wrong!")
            exit()
    if score == 3:
        print("You win!")
    
# main function
if __name__ == "__main__":
    number_guess()
