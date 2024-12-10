class Student:
    def __init__(self,i_d,name,age):
        self.i_d = i_d
        self.name = name
        self.age = age
        self.subject_grade_dic = {}
    def __str__(self):
        return f"id: {self.i_d} \nname: {self.name}\nage: {self.age}\nsubject and grades : {self.subject_grade_dic}"

    def __eq__(self, other):
        return self.i_d == other.i_d

    def __gt__(self, other):
        return self.age > other.age

    def add_grade(self,subject_name,grade):
        self.subject_grade_dic[subject_name]=grade

    def calc_factor(self,subject_name,factor):
        new_grade = 0
        if subject_name not in self.subject_grade_dic:
            print("subject not found!!")
            return
        new_grade = self.subject_grade_dic[subject_name] * (1+factor/100)
        if new_grade > 100:
            new_grade = 100
        self.subject_grade_dic[subject_name]=new_grade

    def average(self):
        """Calculate and return the average grade."""
        if not self.subject_grade_dic:
            return 0
        return sum(self.subject_grade_dic.values()) / len(self.subject_grade_dic)

