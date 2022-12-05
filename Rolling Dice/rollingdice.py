'''Design a project where as an input student will give a static number (between 1 to 6) and then roll the dice which randomly generate an integer value between 1 to 6. The winning situation arrives when the given static/fixed number exactly same to the number came after rolling the dice.'''

import random
import time
score=0
print('Welcome to the dice rolling game!')
while True:
    dice=random.randint(1,6)
    x=input("Do you want to start the game? (Yes/No): ")
    if x=="Yes" or x=="yes":
        while True:
            try:
                number = int(input('Enter a number between 1 and 6: '))
                if number < 1 or number > 6:
                    print('Number must be between 1 and 6!')
                    continue
                break
            except ValueError:
                print('Invalid input!')
                continue
        print('Rolling the dice...')
        time.sleep(2)
        print('The value is:', dice)
        if dice == number:
            score+=1
            print('You win!, your score is',score)
        else:
            print('You lose!')
            print('Better Luck next time :(')
    elif x=="No" or x=="no":
        break
    else:
        print("Invalid Input!")

