from studen_course_ex.Course import Course
from studen_course_ex.Student import Student

course_number = input("Please enter course number: ")
course_name = input("Please enter course name: ")
max_students = int(input("Please enter max students in course: "))
course1 = Course(course_number,course_name,max_students)
subject1 = input("Please enter subject: ")
teacher1 = input("Please enter teacher name: ")
course1.add_sub_teacher(subject1,teacher1)
student_id = input("enter student id: ")

while student_id != '0':
    if not course1.space_in_course():
        break
    student_name = input("enter student name: ")
    subject_name = input("enter subject name: ")
    grade = int(input("enter subject name: "))


    student_id = input("enter student id: ")



# liron = Student('208233650','Liron Lojkin',25)
# moshe = Student('312456345','Moshe Cohen',70)
# liron.add_grade('python',70)
# liron.add_grade('qa',90)
# moshe.add_grade('python',80)
# python_course = Course('1234','python',5)
# python_course.add_student(liron)
# python_course.add_student(moshe)
# #python_course.add_factor('python',10)
# print(python_course.weak_students())






