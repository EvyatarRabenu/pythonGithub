from studen_course_ex.Student import Student

class Course:

    def __init__(self, course_id, course_name, max_student):
        # Initialize a course with ID, name, max students, and empty lists for students and subjects.
        self.subject_teacher_dic = {}
        self.student_list = []
        self.course_id = course_id
        self.course_name = course_name
        self.max_student = max_student

    def __str__(self):
        # Return a string representation of the course details.
        return (f"course number: {self.course_id}\n"
                f"course name: {self.course_name}\n"
                f"max student in course: {self.max_student}\n"
                f"student list: \n{self.student_list}\n"
                f"subject and teachers: {self.subject_teacher_dic}")

    def add_sub_teacher(self, subject_name, teacher):
        # Add a subject and its corresponding teacher to the course.
        self.subject_teacher_dic[subject_name] = teacher

    def space_in_course(self):
        # Check if there is space available for another student in the course.
        return len(self.student_list) < self.max_student

    def add_student(self, student: Student):
        # Add a student to the course if there is space available.
        if len(self.student_list) >= self.max_student:
            print("Course is full of students!!")
            return False
        self.student_list.append(student)
        print(f"Student {student.name} added successfully")
        return True

    def add_factor(self, subject_name, factor):
        # Apply a factor to all students' grades for a specific subject.
        for student in self.student_list:
            student.calc_factor(subject_name, factor)

    def del_student(self, student: Student):
        # Remove a student from the course if they exist in the student list.
        if student not in self.student_list:
            print("Student not in course!!")
            return
        self.student_list.remove(student)

    def averages(self):
        # Calculate and return a dictionary of student IDs and their average grades.
        student_avg_dic = {}
        for student in self.student_list:
            student_avg_dic[student.i_d] = student.average()
        return student_avg_dic

    def weak_students(self):
        # Find and return the IDs of students with the lowest average grade.
        lowest_grades = []
        averages = self.averages()
        if not averages:
            return []  # Handle the case where there are no grades

        lowest_grade_value = min(averages.values())  # Find the minimum grade
        for student_id, grade in averages.items():
            if grade == lowest_grade_value:
                lowest_grades.append(student_id)

        return lowest_grades
