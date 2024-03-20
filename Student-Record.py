


#Question 1 
'''
A) Develop a program in your preferred programming language that begins by asking users to enter the number of student records they would like to create.
You should then proceed to ask the user to fill in the information for each of these students (ID, Name, Grade).
The information should be stored using a compound data structure such as a list.
Finally, your program should output the average, highest and lowest grades for the cohort.
'''
def hridaya():
    record_student = int(input("How many student records would you like to store?"))
    id = []
    student_names = []
    student_grades = []

    for loop in range(record_student):
        student_id = input("Enter the student id: ")
        id.append(student_id)
        name = input("Enter the student name: ")
        student_names.append(name)
        grade = float(input("Enter the student marks: "))
        student_grades.append(grade)
        print("\n")

    average = sum(student_grades)/len(student_grades)
    max_grade = max(student_grades)
    min_grade = min(student_grades)

    print("Average grade is\n"'{:.2f}'.format(average))
    print ("Maximum grade is\n",max_grade)
    print("Minimum grade is\n",min_grade)

hridaya()


#Question 2
'''
B) Extend your program to allow multiple grades to be stored for each student.
For each student, prompt users to enter grades for three modules (4CS001, 4CS015 and 4CI018).
Your program should output the same information as before, but on a per module basis
'''
def hridaya():
    record_student = int(input("How many student records would you like to store?"))
    id = []
    student_names = []
    subject1 = []
    subject2 = []
    subject3 = []

    for loop in range(record_student):
        student_id = input("Enter the student id: ")
        id.append(student_id)
        name = input("Enter the student  name: ")
        student_names.append(name)
        grade1 = float(input("Enter the student marks (4CS001): "))
        subject1.append(grade1)
        grade2 = float(input("Enter the student marks (4CS015): "))
        subject2.append(grade2)
        grade3 = float(input("Enter the student marks (4CI018):"))
        subject3.append(grade3)
        print("\n")

    average_subject1 = sum(subject1)/len(subject1)
    max_grade1 = max(subject1)
    min_grade1 = min(subject1)

    average_subject2 = sum(subject2)/len(subject2)
    max_grade2 = max(subject2)
    min_grade2 = min(subject2)

    average_subject3 = sum(subject3)/len(subject3)
    max_grade3 = max(subject3)
    min_grade3 = min(subject3)


    print("4CS001\n")
    print("Average grade of the subject is\n"'{:.2f}'.format(average_subject1))
    print("Maximum grade of the subject is\n",max_grade1)
    print("Minimum grade of the subject is\n",min_grade1)

    print("4CS015\n")
    print("Average grade of the subject is\n"'{:.2f}'.format(average_subject2))
    print(f"Maximum grade  of the subject is\n",max_grade2)
    print(f"Minimum grade  of the subject is\n",min_grade2)

    print("4CI018\n")
    print("Average grade of the subject is\n"'{:.2f}'.format(average_subject3))
    print(f"Maximum grade  of the subject is\n",max_grade3)
    print(f"Minimum grade of the suject  is\n",min_grade3)
    
hridaya()


#question 3
'''
C) Extend your program such that it stores and retrieves student information from a file on disk to ensure that data created in one session persists to the next and isn’t lost.
You should create two functions, one for storing data and the other for retrieving.
'''






