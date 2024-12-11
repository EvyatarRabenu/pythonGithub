class Student:
    def __init__(self, i_d, name, age, subject_grade_dic):
        """Initialize a student with ID, name, age, and grades dictionary."""

        #check for type errors:
        if type(i_d)!= str:
            raise TypeError('id must be string!')
        if type(name)!= str:
            raise TypeError('name must be string!')
        if type(age)!= int:
            raise TypeError('age must be int!')
        if type(subject_grade_dic)!= dict:
            raise TypeError('subject and grades must be dictionary type!')

        if not (5 <= age <= 120):  # Check if age is within the valid range
            raise ValueError(f"Invalid age: {age}. Age must be between 5 and 120.")

        if not i_d.isdigit() or len(i_d) != 9: # Validate ID length
            raise ValueError("ID must be exactly 9 digits.")

        self.i_d = i_d
        self.name = name
        self.age = age
        self.subject_grade_dic = subject_grade_dic

    def __repr__(self):
        # Return a string representation of the student.
        return f"id: {self.i_d} name: {self.name}"

    def __eq__(self, other):
        # Compare two students by their ID.
        if type(other) != Student:
            raise TypeError('compare only 2 students!')
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
