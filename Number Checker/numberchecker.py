'''In this project you have to enter a range [A, B] and system will randomly pick any number from your given range and check the status of that given number.'''

# Importing the required modules
import random
import requests
import json
import sys

# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    lower_limit = input('Enter the lower limit: ')
    upper_limit = input('Enter the upper limit: ')
    # Calling the function to get the status
    status = number_checker(lower_limit, upper_limit)
    # Printing the status
    print(status)

# Defining the function to check the status of the number
def number_checker(lower_limit, upper_limit):
    '''This function checks the status of the number'''
    # Getting the API key from the file
    with open('api_key.txt', 'r') as file:
        api_key = file.read()
    # Getting the random number
    number = random.randint(int(lower_limit), int(upper_limit))
    # Getting the response from the API
    response = requests.get('http://numbersapi.com/{}/math?json=true&api_key={}'.format(number, api_key))
    # Getting the data from the response
    data = json.loads(response.text)
    # Getting the status
    status = data['found']
    # Returning the status
    return status

# Calling the main function
if __name__ == '__main__':
    main()