'''Your task is to find the name of the student with maximum marks after updation in marks and the jump in the student’s rank i.e., previous rank – current rank. 
You are given three lists` names, mark`s and update`s where: 
    • Names contain the names of students.
    • Marks contain the marks of the same students.
    • Updates contains the integers by which the marks of these students are to be updated.
(Number of levels a student is ranking up or down must be displayed) '''

# taking the input from the user
# if the input is not a number then the program will ask for the input again
while True:
    try:
        N = int(input("Enter the number of students: "))
        break
    except ValueError:
        print("Please enter a number")

# defining a function to find the name of the student with maximum marks after updation in marks and the jump in the student’s rank
def rankmarkcalculator(N):
    # defining the lists
    names = []
    marks = []
    updates = []
    # taking the input from the user
    # if the input is not a number then the program will ask for the input again
    for i in range(N):
        names.append(input("Enter the name of the student: "))
        while True:
            try:
                marks.append(int(input("Enter the marks of the student: ")))
                break
            except ValueError:
                print("Please enter a number")
        while True:
            try:
                updates.append(int(input("Enter the update in marks of the student: ")))
                break
            except ValueError:
                print("Please enter a number")
    # defining the list to store the updated marks
    updatedmarks = []
    # updating the marks
    for i in range(N):
        updatedmarks.append(marks[i]+updates[i])
    # finding the maximum marks
    maxmarks = max(updatedmarks)
    # finding the index of the maximum marks
    index = updatedmarks.index(maxmarks)
    # finding the name of the student with maximum marks
    maxname = names[index]
    # finding the previous rank of the student with maximum marks
    previousrank = updatedmarks.index(maxmarks)+1
    # finding the current rank of the student with maximum marks
    currentrank = updatedmarks.index(maxmarks)+1
    # finding the jump in the student’s rank
    jump = previousrank-currentrank
    # printing the result
    print("The name of the student with maximum marks after updation in marks:",maxname)
    print("The jump in the student’s rank:",jump)

# calling the function
rankmarkcalculator(N)