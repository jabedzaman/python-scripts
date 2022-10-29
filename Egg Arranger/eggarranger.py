'''A basket is given to you in the shape of a matrix. If the size of the matrix is N x N then the range of number of eggs you can put in each slot of the basket is 1 to N2 . You task is to arrange the eggs in the basket such that the sum of each row, column and the diagonal of the matrix remain same.'''

# taking the input from the user
# if the input is not a number then the program will ask for the input again

a = " "
while a.isnumeric() == False:
    a = input("Enter a number: ")
    if a.isnumeric() == False:
        print("Enter a number")

# converting the input into integer

a = int(a)

# defining a function to check if the sum of each row, column and the diagonal of the matrix remain same

def eggarranger(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    i = 0
    j = n//2
    for k in range(1,n**2+1):
        a[i][j] = k
        i = i-1
        j = j+1
        if k%n == 0:
            i = i+2
            j = j-1
        else:
            if i < 0:
                i = n-1
            if j > n-1:
                j = 0
    return a
    
# printing the matrix

for i in eggarranger(a):
    print(i)

    