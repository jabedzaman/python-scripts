# Path: Rock Paper Scissors/rockpaperscissors.py
'''
    rock paper scissors game. if user wins points increase by 1
'''

import random

def main():
    # variables
    user_points = 0
    # create a list of choices
    choices = ['rock', 'paper', 'scissors']
    # get the user's choice
    user_choice = input('Choose rock, paper, or scissors: ')
    # get the computer's choice
    computer_choice = random.choice(choices)
    # determine who won
    if user_choice == computer_choice:
        print('Tie')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('You lose!')
        else:
            print('You win!')
            user_points += 1
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print('You lose!')
        else:
            print('You win!')
            user_points += 1
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('You lose!')
        else:
            print('You win!')
            user_points += 1
    else:
        print('Invalid choice')

    # display what the computer chose
    print('The computer chose', computer_choice + '.')
    # display the user's points
    print('You have', user_points, 'points.')

# call the main function
if __name__ == '__main__':
    main()

