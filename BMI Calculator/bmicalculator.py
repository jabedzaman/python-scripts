'''
    calculates the BMI
'''

def calculate_bmi(weight, height):
    ''' calculates the BMI '''
    return weight / (height * height)

def main():
    ''' main function '''
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in m: "))
    bmi = calculate_bmi(weight, height)
    print("BMI: ", bmi)

if __name__ == "__main__":
    main()

# Path: BMI Calculator/test_bmicalculator.py