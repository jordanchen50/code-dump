##################################################
## Assignment 2: GRADEBOOK
## Author: Jordan Chen
## Email: jordanchen50@gmail.com
## Class: MIS-315 Fall 2020
##################################################

print("Welcome to the gradebook analyzer!")

repeat_analysis = "yes"

# While loop for repeating the entire gradebook analyzer
while repeat_analysis.lower() == "yes":
    
    students = int(input("\nHow many students are in the class? "))
    
    # Check if studnets is negative or not
    while students <= 0:
        print("Invalid number of students. Quantitiy must be at least 1.")
        students = int(input("How many students are in the class? "))
    
    # This variable is to have the studnets increase by one
    students_plus_one = students + 1
    specific_student = 1
    
    class_average = []
    
    # lists for grade ranges A-F
    student_average_a = []
    student_average_b = []
    student_average_c = []
    student_average_d = []
    student_average_f = []
    
    # The while loop will run until the student number and user input number of students match 
    while students_plus_one != specific_student:
        
        repeat_score = "yes"
        student_score = []
        print(" ")
        
        # This while loop is to allow user to enter as many student scores as they want
        while repeat_score.lower() == "yes":
            
            new_student_score = float(input("Enter student " + str(specific_student) + "'s assignment score: "))
            
            # Checker to make sure the scores are between 0 and 100
            if new_student_score < 0 or new_student_score > 100:
                print("Invalid Score. Score range is from 0 to 100.")
            else:
                student_score.append(new_student_score)
            
            repeat_score = input("Enter another score (yes/no)?: ")
        
        # Calculations for specific student average 
        count = len(student_score)
        total = sum(student_score)
        average = total / count
        class_average.append(average)
        
        print("\nStudnet " + str(specific_student) + "'s average was: " + str(average))
        
        # Sorts the student average score into it's respective grade letter list
        if average >= 90:
            student_average_a.append(average)
        elif average < 90 and average >= 80:
            student_average_b.append(average)
        elif average < 80 and average >=70:
            student_average_c.append(average)
        elif average < 70 and average >= 60:
            student_average_d.append(average)
        else:
            student_average_f.append(average)
        
        # This makes the while loop eventually end when the student number and user input number of students match 
        specific_student = specific_student + 1
    
    # Calcualtions for class average
    class_count = len(class_average)
    class_total = sum(class_average)
    class_average = class_total / class_count
    
    print("\nClass Average:", class_average)
    
    # Print outs for number of letter grades 
    a = len(student_average_a)
    print("\nA's:",a)
    b = len(student_average_b)
    print("B's:",b)
    c = len(student_average_c)
    print("C's:",c)
    d = len(student_average_d)
    print("D's:",d)
    f = len(student_average_f)
    print("F's:",f)
    
    # Allows user to run gradebook analyzer as many times as they want
    repeat_analysis = input("\nWould you like to analyze another class (yes/no)?: ")

# Outside of while loop, only runs when user is done using the analyzer 
print("\nThank you for using the gradebook analyzer!")