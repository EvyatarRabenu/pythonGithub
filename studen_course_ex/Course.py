from studen_course_ex.Student import Student


class Course:

    def __init__(self,course_id,course_name,max_student):
        self.subject_teacher_dic = {}
        self.student_list = []
        self.course_id = course_id
        self.course_name = course_name
        self.max_student = max_student

    def __str__(self):
        return (f"course number: {self.course_id}\n"
                f"course name: {self.course_name}\n"
                f"max student in course: {self.max_student}\n"
                f"student list: \n{self.student_list}"
                f"subject and teachers: {self.subject_teacher_dic}")

    def add_student(self,student:Student):
        if len(self.student_list)+1 > self.max_student:
            print("Course is full of students!!")
            return False
        self.student_list.append(student)
        print(f"Student {student.name} added successfully")
        return True

    def add_factor(self,subject_name,factor):
        for student in self.student_list:
            student.calc_factor(subject_name,factor)

