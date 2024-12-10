class Course:

    def __init__(self,course_id,course_name,max_student):
        self.subject_teacher_dic = {}
        self.student_list = []
        self.course_id = course_id
        self.course_name = course_name
        self.max_student = max_student