'''Create a multiplication table application where user will enter a sentinel value n and the application will display the mathematical multiplication tables till given sentinel value n.'''

# Importing the required modules
import sys

# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    sentinel_value = input('Enter the sentinel value: ')
    # Calling the function to get the result
    result = multiplication_table(sentinel_value)
    # Printing the result
    print(result)

# Defining the function to get the multiplication table
def multiplication_table(sentinel_value):
    '''This function gets the multiplication table'''
    # Converting the sentinel value to int
    sentinel_value = int(sentinel_value)
    # Getting the multiplication table
    for number in range(1, sentinel_value + 1):
        for multiplier in range(1, 11):
            result = number * multiplier
            print(number, 'x', multiplier, '=', result)
        print('')
    # Returning the result
    return result

# Calling the main function
if __name__ == '__main__':
    main()