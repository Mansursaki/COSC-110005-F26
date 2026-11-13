# Mansur Sakhizadah 
# November 3th 2026


# Ask the user for class exercise marks and test 1 marks 
# Store class exercise marks in a python list 
# use loops to collect multiple marks 
# accept class exercise marks from 0-3 and test 1 marks from 0-25
# calculate percentage and apply assignment weight 
# display each assignment type 




# Start

# Create an empty list to store class execrise
# FOR each Class Exercise
#     Ask the user to enter their mark    
#     WHILE mark is less than 0 or greater than 3
#         Display "Invaild mark. Please try again."
#         Ask the user to enter their mark again
#     END WHILE
# END FOR   
# Ask the user to enter their Test 1 mark
# WHILE test 1 mark is less than 0 OR greater than 25
#     Display "Invaild mark. Please try again."
#     Ask the user to enter their Test 1 mark again  
# END WHILE
# Add mark to class_marks list
# Add together all marks in class_marks list

# Divide the total by the maximum possible marks 
# and multiply by 100 to get the Class exercise percentage
# Divide the test 1 mark by 25

# Multiply the result by 100 to get the Test 1 percentage
# Calculate Class Exercise weighted mark using 20% 

# Calculate Test 1 weighted mark using 16%

# Add both weighted marks together  

# Divide the total by 36 to get the midterm percentage

# Display Class exercise percentage 

# Display test 1 percentage

# Display overall midterm percentage 

# END


class_marks=[]

for count in range(4):
    mark= float(input("Enter Class Exercise mark:"))
    while mark < 0 or mark > 3:
        print("Invalid mark. Please try again")
        mark = float(input("Enter Class Exercise mark again"))
    class_marks.append(mark)

test1_mark = float(input("Enter your Test 1 mark"))

while test1_mark < 0 or test1_mark > 25:
    print("Invalid Test 1 mark. Please try again.")
    test1_mark = float(input("Enter your test 1 mark again."))

class_total = sum(class_marks)
class_percentage = (class_total / 12) * 100
test1_percentage = (test1_mark / 25) * 100
midterm_percentage = ((class_percentage * 20) + (test1_percentage * 16)) / 36
print ("Class Exercise Percentage:", round(class_percentage, 2), "%")
print("Test 1 Percentage:", round(test1_percentage, 2), "%")
print("Overall Midterm Percentage:", round(midterm_percentage, 2), "%")





