'''The task is to generate a random story every time user runs the program.'''

# Importing the required modules
import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

# Defining the main function
def main():
    '''This is the main function'''
    print(random.choice(when), random.choice(who), random.choice(went), random.choice(happened))

# Calling the main function
if __name__ == '__main__':
    main()