'''You task is to replicate the working of ATM for a single user, let’s say, Mr. John, who has already successfully logged into her account on the ATM Machine, now, we will program the next steps he may want to perform. 
Like display his name and cash available in his savings account
Withdraw cash and display the status of the cash balance.
Deposit cash and display the status of the cash balance.
(Your task is to design and implement the ATM functionality by taking care of all constraints, for example if minimum cash available is less than 5000 then system will display low balance)'''

# importing the random module
import random

# defining a function to replicate the working of ATM
def atmclone():
    # defining the list to store the cash available in the savings account
    cash = []
    # taking the input from the user
    # if the input is not a number then the program will ask for the input again
    while True:
        try:
            N = int(input("Enter the number of times you want to enter the cash available in the savings account: "))
            break
        except ValueError:
            print("Please enter a number")
    # taking the input from the user
    # if the input is not a number then the program will ask for the input again
    for i in range(N):
        while True:
            try:
                cash.append(int(input("Enter the cash available in the savings account: ")))
                break
            except ValueError:
                print("Please enter a number")
    # defining the list to store the cash available in the savings account
    updatedcash = []
    # updating the cash available in the savings account
    for i in range(N):
        updatedcash.append(cash[i]+random.randint(1000,10000))
    # printing the cash available in the savings account
    print("The cash available in the savings account:",updatedcash)
    # defining the list to store the cash withdrawn
    withdrawn = []
    # taking the input from the user
    # if the input is not a number then the program will ask for the input again
    for i in range(N):
        while True:
            try:
                withdrawn.append(int(input("Enter the cash withdrawn: ")))
                break
            except ValueError:
                print("Please enter a number")
    # defining the list to store the cash deposited
    deposited = []
    # taking the input from the user
    # if the input is not a number then the program will ask for the input again
    for i in range(N):
        while True:
            try:
                deposited.append(int(input("Enter the cash deposited: ")))
                break
            except ValueError:
                print("Please enter a number")
    # defining the list to store the cash balance
    cashbalance = []
    # calculating the cash balance
    for i in range(N):
        cashbalance.append(updatedcash[i]-withdrawn[i]+deposited[i])
    # printing the cash balance
    print("The cash balance:",cashbalance)
    # defining the list to store the status of the cash balance
    status = []
    # calculating the status of the cash balance
    for i in range(N):
        if cashbalance[i] < 5000:
            status.append("low balance")
        else:
            status.append("high balance")
    # printing the status of the cash balance
    print("The status of the cash balance:",status)

# calling the function
atmclone()

