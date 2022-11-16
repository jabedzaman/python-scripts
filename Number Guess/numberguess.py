'''The task is to create a script that generates a random number between a fixed range, and  if the user guesses the number right in three chances, then user wins otherwise user lose.'''

# Path: Number Guess/numberguess.py

#Import required module
import random
while True:
    
    #Initially the number of attempts=0
    attempts=0
    
    #Taking the lower and upper limits of range from the user.
    n1=int(input("Enter the lower limit of range: "))
    n2=int(input("Enter the upper limit of range: "))
    
    #Generate a random integer between n1 and n2.
    s=random.randint(n1,n2)
    i=1
    
    #Maximum chance=3
    while i<=3:
        attempts+=1
        c=int(input("Guess a number: "))
        if c>s:
            if attempts==3:
                print("Better Luck Next Time!")
                break
            else:
                print("Have one more try! Your guess was too high")
        elif c<s:
            if attempts==3:
                print("Better Luck Next Time!")
                break
            else:
                print("Have one more try! Your guess was too small")
        else:
            print("Congrats! You got it right in",i,"attempts.")
            break
        i+=1
