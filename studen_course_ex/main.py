from studen_course_ex.Course import Course
from studen_course_ex.Student import Student

liron = Student('208233650','Liron Lojkin',25)
moshe = Student('208233655','Moshe Cohen',70)
liron.add_grade('python',70)
liron.add_grade('qa',90)
moshe.add_grade('python',80)
python_course = Course('1234','python',5)
python_course.add_student(liron)
python_course.add_student(moshe)
python_course.add_factor('python',10)
print(liron.subject_grade_dic)
print(moshe.subject_grade_dic)




