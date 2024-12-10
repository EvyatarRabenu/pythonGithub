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
                f"student list: \n{self.student_list}\n"
                f"subject and teachers: {self.subject_teacher_dic}")

    def add_sub_teacher(self,subject_name,teacher):
        self.subject_teacher_dic[subject_name]=teacher

    def space_in_course(self):
        if len(self.student_list)+1>self.max_student:
            return False
        return True

    def add_student(self, student: Student):
        if len(self.student_list) >= self.max_student:
            print("Course is full of students!!")
            return False
        self.student_list.append(student)
        print(f"Student {student.name} added successfully")
        return True

    def add_factor(self,subject_name,factor):
        for student in self.student_list:
            student.calc_factor(subject_name,factor)

    def del_student(self,student:Student):
        if student not in self.student_list:
            print("Student not in course!!")
            return
        self.student_list.remove(student)

    def averages(self):
        student_avg_dic={}
        for student in self.student_list:
            student_avg_dic[student.i_d] = student.average()
        return student_avg_dic

    def weak_students(self):
        lowest_grades=[]
        averages = self.averages()  # Assuming this returns a dictionary {id: grade}
        if not averages:
            return []  # Handle the case where there are no grades

        # Find the minimum grade
        lowest_grade_value = min(averages.values())

        # Collect the IDs of students with the lowest grade
        #lowest_grades = [student_id for student_id, grade in averages.items() if grade == lowest_grade_value]
        for student_id,grade in averages.items():
            if grade == lowest_grade_value:
                lowest_grades.append(student_id)

        return lowest_grades





