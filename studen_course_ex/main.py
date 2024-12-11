from studen_course_ex.Course import Course
from studen_course_ex.Student import Student




# Get basic course details from the user
try:
    student = Student("123", "liron", 20, {"Math": 90})
except ValueError as e:
    print(e)  # Output: Invalid age: 3. Age must be between 5 and 120.
course_number = input("Please enter course number: ")
course_name = input("Please enter course name: ")
max_students = int(input("Please enter max students in course: "))
course1 = Course(course_number, course_name, max_students)

# Add subjects and their teachers to the course
num_of_subs = int(input("Please enter how many subjects you want to enter: "))
for _ in range(num_of_subs):
    subject = input("Please enter subject name: ")
    teacher = input("Please enter teacher name: ")
    course1.add_sub_teacher(subject, teacher)

# Add students to the course until the user stops or the course is full
student_id = input("Enter student ID: ")
while student_id != '0':
    student_grades = {}
    if not course1.space_in_course():  # Check if the course has space for new students
        print("Class is full!!")
        break

    # Collect student details
    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))

    # Collect grades for each subject
    for subject in course1.subject_teacher_dic:
        grade = int(input(f"Enter your grade for {subject}: "))
        student_grades[subject] = grade

    # Create a student object and add them to the course
    student = Student(student_id, student_name, student_age, student_grades)
    if not course1.add_student(student):  # Try to add the student to the course
        break
    student_id = input("Enter student ID: ")

# Print the current list of students
print()
print(course1.student_list)
print()

# Apply a factor to grades for a specific subject
factor_subject = input("Please enter subject name for factor: ")
factor = int(input("Please enter factor percentage: "))
print()
course1.add_factor(factor_subject, factor)  # Add the factor to grades
print(course1.student_list[0].subject_grade_dic)  # Print updated grades
print()

# Identify and remove the weakest students from the course
lowest_students = course1.weak_students()  # Get IDs of the weakest students
for student_id in lowest_students:
    # Find the student object with the matching ID
    student_to_remove = next((s for s in course1.student_list if s.i_d == student_id), None)
    if student_to_remove:  # Remove the student if found
        course1.del_student(student_to_remove)

# Print the updated student list
print(course1.student_list)
print()

# Find and print the oldest student in the course
oldest_student = course1.student_list[0]
for student in course1.student_list:
    if oldest_student < student:  # Compare ages using the overridden `__gt__` method
        oldest_student = student
print(oldest_student)
print()

# Print the course details
print(course1)
