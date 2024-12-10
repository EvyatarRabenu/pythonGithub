from studen_course_ex.Course import Course
from studen_course_ex.Student import Student

course_number = input("Please enter course number: ")
course_name = input("Please enter course name: ")
max_students = int(input("Please enter max students in course: "))
course1 = Course(course_number,course_name,max_students)

num_of_subs = int(input("please enter how many subjects you want to enter: "))
for _ in range(num_of_subs):
    subject = input("Please enter subject name: ")
    teacher = input("Please enter teacher name: ")
    course1.add_sub_teacher(subject,teacher)


student_id = input("enter student id: ")

while student_id != '0':
    student_grades = {}
    if not course1.space_in_course():
        print("class is full!!")
        break

    student_name = input("enter student name: ")
    student_age = int(input("enter student age: "))

    for subject in course1.subject_teacher_dic:
        grade = int(input(f"enter your grade for {subject}: "))
        student_grades[subject]=grade
    student = Student(student_id,student_name,student_age,student_grades)
    #students_list.append(student)
    if not course1.add_student(student):
        break
    student_id = input("enter student id: ")

print()
print(course1.student_list)
print()

factor_subject = input("please enter subject name for factor: ")
factor = int(input("please enter factor present: "))
print()

course1.add_factor(factor_subject,factor)
print(course1.student_list[0].subject_grade_dic)
print()

lowest_students = course1.weak_students()  # Get IDs of the weakest students

for student_id in lowest_students:
    # Find the Student object by looping through the list
    student_to_remove = None
    for s in course1.student_list:
        if s.i_d == student_id:
            student_to_remove = s
            break  # Stop searching once the student is found

    # Remove the student if found
    if student_to_remove:
        course1.del_student(student_to_remove)

# Print the updated student list
print(course1.student_list)
print()


oldest_student = course1.student_list[0]
for student in course1.student_list:
    if oldest_student<student:
        oldest_student=student
print(oldest_student)
print()
print(course1)
