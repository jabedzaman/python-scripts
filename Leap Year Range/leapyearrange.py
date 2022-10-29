'''Your task to create a functionality in which when user will input a range of two dates. Then your module will find and print all years in the range of given dates those are leap years separately and rest of the years those are non-leap separately.
For example:
Input date range in the format dd/mm/yyyy
(12/01/2000) to (13/12/2025)
Leaps years are:
2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048.
Non leap years are:
2001,2002,2005,2006,2007-----------------------------------------------------------------------
(Student is free to decide the input and output layout for this mini project)'''


print("Enter the range of dates in the format dd/mm/yyyy")
print("press ctrl+c to exit the program anytime")


# taking the starting year and validating the fromat
# if the format is not correct then the program will ask for the input again

a = " "
while len(a) != 10 :
    a = input("Enter the starting year: ")
    if len(a) != 10:
        print("Enter the date in the correct format")     

       
# taking the ending year and validating the format
# if the format is not correct then the program will ask for the input again
    
b = " "
while len(b) != 10 :
    b = input("Enter the ending year: ")
    if len(b) != 10:
        print("Enter the date in the correct format")


# printing of leap years and non leap years

a = int(a[-4:])
b = int(b[-4:])
print("Leap years are: ")
for i in range(a,b+1):
    if i%4==0:
        print(i, end=" ")
print("Non leap years are: ")
for i in range(a,b+1):
    if i%4!=0:
        print(i, end=" ")

