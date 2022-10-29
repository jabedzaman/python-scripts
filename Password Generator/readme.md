# Password generator

This is a simple password generator that generates a password of a given length. It uses the `random` module to generate a random number between 0 and 1, and then multiplies it by the length of the string of characters that you want to use to generate the password. It then rounds the number down to the nearest integer, and uses that integer as the index of the character that it will add to the password. It repeats this process until the password is the desired length.
