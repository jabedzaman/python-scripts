'''Clock Angle Problem
Clock Angle Problem: Given time in hh:mm format in 24-hour notation, calculate the shorter angle between the hour and minute hand in an analog clock.
Input:  5:30
Output: 15°
Input:  21:00
Output: 90° 
Input:  12:00
Output: 0° '''

# Path: Clock Angle/clockangle.py

# taking the input from the user
# if the format is not correct then the program will ask for the input again

a = " "
while len(a) != 5 :
    a = input("Enter the time in the format hh:mm: ")
    if len(a) != 5:
        print("Enter the time in the correct format")

# converting the input into hours and minutes

a = a.split(":")
hours = int(a[0])
minutes = int(a[1])

# calculating the angle between the hour and minute hand

angle = abs((hours*30 + minutes*0.5) - (minutes*6))

# printing the angle

print("The angle between the hour and minute hand is: ", angle)
