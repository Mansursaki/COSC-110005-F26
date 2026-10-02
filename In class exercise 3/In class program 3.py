# Mansur Sakhizadah
# October 1st 2026
# Description: This program will be used to check students information to see if its valid or invalid   



# Output a working program that shows only valid values for these attributes

# Input Student name, Student ID, Number of courses enrolled in, Execrise marks

# Process 
# 1. ask user to input student name 
# 2. if the name is invalied display error message and try again   
# 3. ask the user to input Student ID
# 4. check if student ID contains 9 digit numbers
# 6. if student ID is invailed display error message and try again  
# 7. ask the user to input amount of courses enrolled in 
# 8. check if the number is between 1-8
# 9. if the number is invailed dispay and error message and try again 
# 10. ask the user to input their excersie number 
# 11. Check if mark is between 1-100
# 12. if mark is invailed display error message 

# pseudo code 
#
#ASK for student name
#IF student name is blank or only spaces
#   DISPLAY error message
#ELSE
#    DISPLAY student name accepted
#ASK for student ID
#IF student ID does not contain 9 digits
#   DISPLAY error message
#ELSE
#    DISPLAY student ID accepted
#ASK for number of courses
#IF number of courses is less than 1 or more than 8
#   DISPLAY error message
#ELSE
#    DISPLAY number of courses accepted
#ASK for exercise mark
# IF exercise mark is less than 0 or more than 100
#    DISPLAY error message
# ELSE
#     DISPLAY exercise mark accepted
#  
# 
#        

student_name = input("Enter student name:")

if student_name == "":
    print("Error: Student name cannot be blank.")
else:
    print("Student name accepted.")


student_id = input ("Enter student ID:")

if len(student_id) != 9:
    print ("Error: Student ID must contain only 9 digits please try again.")
else:
    print("Student ID accepted.")


number_of_courses = int(input("Enter number of courses: "))

if number_of_courses < 1 or number_of_courses > 8:
    print("Error: Number of courses must be from 1 to 8.")
else:
    print("Number of courses accepted.")    


exercise_mark = int(input("Enter exercise mark: "))

if exercise_mark < 0 or exercise_mark > 100:
    print("Error: Exercise mark must be from 0 to 100.")
else:
    print("Exercise mark accepted.")