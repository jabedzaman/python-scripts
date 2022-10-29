'''In this project you have to enter a positive integer range [A, B] and system will find out the status (Prime or composite) of each number available in the given range. At the end print the count also.'''

# Importing the required modules
import sys

# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    range_ = input('Enter the range: ')
    # Calling the function to get the result
    result = prime_composite(range_)
    # Printing the result
    print(result)

# Defining the function to get the prime or composite numbers
def prime_composite(range_):
    '''This function gets the prime or composite numbers'''
    # Converting the range to list
    range_ = range_.split(',')
    # Getting the first number
    first_number = int(range_[0])
    # Getting the second number
    second_number = int(range_[1])
    # Getting the prime or composite numbers
    for number in range(first_number, second_number + 1):
        # Checking the number is prime or composite
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    result = 'Composite'
                    break
            else:
                result = 'Prime'
        else:
            result = 'Composite'
        # Printing the result
        print(number, 'is', result)
    # Returning the result
    return result

# Calling the main function
if __name__ == '__main__':
    main()