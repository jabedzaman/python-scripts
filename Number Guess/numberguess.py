import random
while True:
    attempts=0
    x=input("Do you want to start the game? (Yes/No): ")
    if x=="Yes" or x=="yes":
        n1=int(input("Enter the upper limit: "))
        n2=int(input("Enter the lower limit: "))
        s=random.randint(n1,n2)
        i=1
        while i<=3:
            attempts+=1
            c=int(input("Guess a number: "))
            if c>s:
                if attempts==3:
                    print("Better luck next time!")
                    break
                else:
                    print("Your guess is too high")
            elif c<s:
                if attempts==3:
                    print("Better luck next time!")
                    break
                else:
                    print("Your guess is too high")
            else:
                print("You got it right in",i,"attempts")
                break
        i+=1
    elif x=="No" or x=="no":
        break
    else:
        print("Invalid Input!")
