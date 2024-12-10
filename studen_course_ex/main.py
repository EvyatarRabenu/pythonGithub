from studen_course_ex.Student import Student

liron = Student('208233650','Liron Lojkin',25)
moshe = Student('208233655','Moshe Cohen',70)
liron.add_grade('python',100)
liron.add_grade('qa',90)
liron.add_grade('math',80)


print(moshe > liron)

