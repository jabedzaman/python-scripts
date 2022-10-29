'''Email Slicer is just a simple tool that will take multiple email address as an input and slice it to produce the username and the domain associated with it. The email must be divided into two strings by using @ as the separator'''

# Path: Email Slicer/emailslicer.py

def email_slicer(email):
    username, _, domain = email.strip().partition("@")
    return f"Your username is {username} and domain is {domain}"

# main function
if __name__ == "__main__":
    email = input("Please enter your email address: ")
    print(email_slicer(email))