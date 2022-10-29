'''In this project user will enter single or multiple numbers and your system will predict that the entered number or number’s is/are valid number(s) in a Fibonacci series or not.'''

# Importing the required modules
import sys

# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    numbers = input('Enter the numbers: ')
    # Calling the function to get the result
    result = fibonacci_series(numbers)
    # Printing the result
    print(result)

# Defining the function to check the numbers in the Fibonacci series
def fibonacci_series(numbers):
    '''This function checks the numbers in the Fibonacci series'''
    # Converting the numbers to list
    numbers = numbers.split(',')
    # Getting the first two numbers
    first_number = 0
    second_number = 1
    # Iterating through the numbers
    for number in numbers:
        # Converting the number to int
        number = int(number)
        # Checking the number in the Fibonacci series
        if number == first_number or number == second_number:
            result = 'Valid'
        else:
            result = 'Invalid'
            break
        # Getting the next number
        next_number = first_number + second_number
        # Updating the first number
        first_number = second_number
        # Updating the second number
        second_number = next_number
    # Returning the result
    return result

# Calling the main function
if __name__ == '__main__':
    main()