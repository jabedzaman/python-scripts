'''You need to write a python script that generates an acronym word from a given sentence.'''

# Importing the required modules

import re
import sys

# Defining the function to generate the acronym

def acronym_generator(sentence):
    '''This function generates an acronym from a given sentence'''
    acronym = ''
    for word in sentence.split():
        acronym += word[0].upper()
    return acronym

# Defining the main function

def main():
    '''This is the main function'''
    sentence = input('Enter a sentence: ')
    print(acronym_generator(sentence))

# Calling the main function

if __name__ == '__main__':
    main()
    