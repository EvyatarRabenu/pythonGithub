class Student:
    def __init__(self, i_d, name, age, subject_grade_dic):
        # Initialize a student with ID, name, age, and grades dictionary.
        self.i_d = i_d
        self.name = name
        self.age = age
        self.subject_grade_dic = subject_grade_dic

    def __repr__(self):
        # Return a string representation of the student.
        return f"id: {self.i_d} name: {self.name}"

    def __eq__(self, other):
        # Compare two students by their ID.
        return self.i_d == other.i_d

    def __gt__(self, other):
        # Compare two students by their age.
        return self.age > other.age

    def add_grade(self, subject_name, grade):
        # Add or update the grade for a specific subject.
        self.subject_grade_dic[subject_name] = grade

    def calc_factor(self, subject_name, factor):
        # Apply a factor to a subject's grade (capped at 100).
        if subject_name not in self.subject_grade_dic:
            print("subject not found!!")
            return
        new_grade = self.subject_grade_dic[subject_name] * (1 + factor / 100)
        self.subject_grade_dic[subject_name] = min(new_grade, 100)

    def average(self):
        # Calculate and return the average grade.
        if not self.subject_grade_dic:
            return 0
        return sum(self.subject_grade_dic.values()) / len(self.subject_grade_dic)
