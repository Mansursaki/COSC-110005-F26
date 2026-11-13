# Mansur Sakhizadah 
# November 11, 2026


# presucode 

#START


# Define get_mark ()
      #Ask the user to enetr a mark
      #Check if mark is vaild
      #If invaild, ask again
      #Return mark

# define calculate_grade()
      #Calculate Class Exercise percentage
      #Calculate Test 1 percentage 
      #Calculate overall Midterm percentage
      #Return results

#Define main()
     #Create an empty list for Class Exercise marks 

#FOR each of the 4 Class Exercise marks

     #Call get_mark()
     #Store mark in list
#END FOR
# 
# Call get _mark () for Test 1 
# 
# Call calculate_grade()
# 
# Display Class Exercise percentage
# Display Test 1 percentage 
# Display overall Midterm percentage 
# 
#END    


#Function to get and validate marks
def get_mark(prompt, maximum):
    mark = float(input(prompt))

    while mark < 0 or mark > maximum:
        print("Invaild mark. Please try agian.")
        mark = float(input(prompt))

    return mark

# Function to calculate grades
def calculate_grade(class_marks, test1_mark):
    class_total = sum(class_marks)

    class_percentage = (class_total / 12) * 100

    test1_percentage = (test1_mark / 25) * 100

    midterm_percentage = ((class_percentage * 20) + (test1_percentage * 16)) / 36

    return class_percentage, test1_percentage, midterm_percentage


# Main program
def main():
    class_marks = []

    # Get four Class exercise marks
    for count in range (4):
        mark = get_mark("enter class exercise mark: ", 3)
        class_marks.append(mark)

    # get test 1 mark
    test1_mark = get_mark("Enter Test 1 mark: ", 25)

    # Calculate grades
    class_percentage, test1_percentage, midterm_percentage = calculate_grade(class_marks, test1_mark)

    # Display results
    print("Class exercise percentage:", round(class_percentage, 2), "%")
    print("Test 1 Percentage:", round(test1_percentage, 2), "%")
    print("Overall Midterm Percentage:", round(midterm_percentage, 2), "%")


main()

     
        
