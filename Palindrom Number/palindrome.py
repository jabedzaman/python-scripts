'''Your task is to write a program to find the nth prime palindrome number, n is the input user will give.'''

# taking the input from the user
# if the input is not a number then the program will ask for the input again

a = " "
while a.isnumeric() == False:
    a = input("Enter a number: ")
    if a.isnumeric() == False:
        print("Enter a number")

# converting the input into integer

a = int(a)

# defining a function to check if the number is prime or not

def prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

# defining a function to check if the number is palindrome or not

def palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

# defining a function to find the nth prime palindrome number

def nthprimepalindrome(n):
    count = 0
    i = 1
    while count != n:
        i += 1
        if prime(i) and palindrome(i):
            count += 1
    return i

# printing the nth prime palindrome number

print("The",a,"th prime palindrome number is: ", nthprimepalindrome(a))

