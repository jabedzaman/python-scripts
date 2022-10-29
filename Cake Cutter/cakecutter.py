'''Your task is to find if it is possible to cut the cake in the below mentioned ways for a given value of N.
Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border. Also, the angle between any two cuts must be a positive integer. Two pieces are equal if their appropriate angles are equal. 
The given cake can be cut in following three ways: 
    • Cut the cake into N equal pieces.
    • Cut the cake into N pieces of any size.
    • Cut the cake into N pieces such that no two of them are equal.'''

# taking the input from the user
# if the input is not a number then the program will ask for the input again
while True:
    try:
        N = int(input("Enter the value of N: "))
        break
    except ValueError:
        print("Please enter a number")

# defining a function to check if the cake can be cut into N equal pieces
def equal(N):
    if N == 1:
        return True
    else:
        return False

# defining a function to check if the cake can be cut into N pieces of any size
def anysize(N):
    if N == 1:
        return True
    else:
        return False

# defining a function to check if the cake can be cut into N pieces such that no two of them are equal
def nonequal(N):
    if N == 1:
        return True
    else:
        return False

# printing the result
print("The cake can be cut into",N,"equal pieces:",equal(N))
print("The cake can be cut into",N,"pieces of any size:",anysize(N))
print("The cake can be cut into",N,"pieces such that no two of them are equal:",nonequal(N))
