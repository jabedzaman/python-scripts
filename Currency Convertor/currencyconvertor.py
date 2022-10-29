'''Your task is to build a currency converter that will allow you to convert currencies from one unit to another, such as converting Indian rupee into pounds, euros, US dollar, Canadian dollar, Chinese yuan, Russia’s Rubal, etc. or vice versa.'''

# Importing the required modules
import requests
import json
import sys
# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    amount = input('Enter the amount: ')
    from_currency = input('Enter the currency you want to convert from: ')
    to_currency = input('Enter the currency you want to convert to: ')
    # Calling the function to get the converted amount
    converted_amount = convert_currency(amount, from_currency, to_currency)
    # Printing the converted amount
    print(converted_amount)
# Defining the function to convert the currency
def convert_currency(amount, from_currency, to_currency):
    '''This function converts the currency'''
    # Getting the API key from the file
    with open('api_key.txt', 'r') as file:
        api_key = file.read()
    # Getting the response from the API
    response = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(from_currency, to_currency, api_key))
    # Getting the data from the response
    data = json.loads(response.text)
    # Getting the exchange rate
    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    # Converting the amount to float
    amount = float(amount)
    # Converting the amount to the new currency
    converted_amount = amount * float(exchange_rate)
    # Returning the converted amount
    return converted_amount
# Calling the main function
if __name__ == '__main__':
    main()
