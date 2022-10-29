'''You have to create a repository of your classmate’s name and mobile number’s. And whenever you want to search the mobile/contact number of some of your classmate, you can easily search it out from the repository you maintained.'''

# Importing the required modules
import sys

# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    name = input('Enter the name: ')
    # Calling the function to get the contact number
    contact_number = contact_list(name)
    # Printing the contact number
    print(contact_number)

# Defining the function to get the contact number
def contact_list(name):
    '''This function gets the contact number'''
    # Getting the contact list
    contact_list = {
        'Rahul': '9876543210',
        'Raj': '1234567890',
        'Ravi': '2345678901',
        'Ramesh': '3456789012',
        'Rajesh': '4567890123',
        'Rakesh': '5678901234',
        'Raju': '6789012345',
        'Rajkumar': '7890123456',
        'Rajendra': '8901234567',
        'Rajeshwari': '9012345678',
        'Rajkumari': '0123456789',
        'Rajani': '1234567891',
        'Rajkumar': '2345678912',
        'Rajesh': '3456789123',
        'Rajkumar': '4567891234',
        'Rajesh': '5678912345',
        'Rajkumar': '6789123456',
        'Rajesh': '7891234567',
        'Rajkumar': '8912345678',
        'Rajesh': '9123456789',
        'Rajkumar': '1234567890',
        'Rajesh': '2345678901',
        'Rajkumar': '3456789012',
        'Rajesh': '4567890123',
        'Rajkumar': '5678901234',
        'Rajesh': '6789012345',
        'Rajkumar': '7890123456',
        'Rajesh': '8901234567',
        'Rajkumar': '9012345678',
        'Rajesh': '0123456789',
        'Rajkumar': '1234567891',
        'Rajesh': '2345678912',
        'Rajkumar': '3456789123',
        'Rajesh': '4567891234',
        'Rajkumar': '5678912345',
        'Rajesh': '6789123456',
        'Rajkumar': '7891234567',
        'Rajesh': '8912345678',
    }
    # Getting the contact number
    contact_number = contact_list[name]
    # Returning the contact number
    return contact_number

# Calling the main function
if __name__ == '__main__':
    main()