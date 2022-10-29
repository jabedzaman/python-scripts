'''Create a program that takes the length of the password as input and generates a random password of the same length. The strength of the password depends equally on the 4 properties mentioned below. If the password generated randomly following the rules or constraints given below, then that password is treated as good in terms of strength and accepted otherwise ignore that password.'''

# Path: Password Generator/passwordgenrator.py

import random
import string

def password_generator(length):
    # list of all the characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # generate a random password
    password = "".join(random.choice(characters) for i in range(length))
    # check if the password is strong
    if check_password(password):
        return password
    else:
        return password_generator(length)
    
def check_password(password):
    # check if the password is strong
    if (any(char.islower() for char in password) and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in string.punctuation for char in password)):
        return True
    else:
        return False
    
# main function
if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    print(password_generator(length))