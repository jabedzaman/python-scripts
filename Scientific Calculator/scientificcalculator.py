'''You task is to build a scientific calculator that performs all the below listed functionalities.'''

# Importing the required modules
import math
import sys
# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    number = input('Enter the number: ')
    option = input('Enter the option: ')
    # Calling the function to get the result
    result = scientific_calculator(number, option)
    # Printing the result
    print(result)
# Defining the function to perform the scientific calculations
def scientific_calculator(number, option):
    '''This function performs the scientific calculations'''
    # Converting the number to float
    number = float(number)
    # Performing the calculations
    if option == 'sin':
        result = math.sin(number)
    elif option == 'cos':
        result = math.cos(number)
    elif option == 'tan':
        result = math.tan(number)
    elif option == 'log':
        result = math.log(number)
    elif option == 'log10':
        result = math.log10(number)
    elif option == 'sqrt':
        result = math.sqrt(number)
    elif option == 'ceil':
        result = math.ceil(number)
    elif option == 'floor':
        result = math.floor(number)
    elif option == 'exp':
        result = math.exp(number)
    else:
        result = 'Invalid option'
    # Returning the result
    return result
# Calling the main function
if __name__ == '__main__':
    main()