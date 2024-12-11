from unittest import TestCase

from studen_course_ex.Student import Student



class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('208233650','liron',25,{'Math':90,'English':80})


    #Start initialize students args tests ---------------------------------------------------------------------------
    def test_id_type(self):
        with self.assertRaises(TypeError):
            stud = Student(10,'liron',25,{'Math':90,'English':80})

    def test_name_type(self):
        with self.assertRaises(TypeError):
            stud = Student('208233650', 10, 25, {'Math': 90, 'English': 80})

    def test_age_type(self):
        with self.assertRaises(TypeError):
            stud = Student('208233650', 'liron', 'abc', {'Math': 90, 'English': 80})

    def test_subject_grade_dic_type(self):
        """check dictionary type"""
        with self.assertRaises(TypeError):
            stud = Student('208233650', 'liron', 25, 43)

    def test_valid_age_lower_limit(self):
        stud=Student('208233650','liron',5,{})
        self.assertEqual(5,stud.age)

    def test_valid_age_upper_limit(self):
        stud=Student('208233650','liron',120,{})
        self.assertEqual(120,stud.age)

    def test_valid_age_middle(self):
        stud=Student('208233650','liron',50,{})
        self.assertEqual(50,stud.age)

    def test_invalid_age_lower_limit(self):
        with self.assertRaises(ValueError):
            stud = Student('208233650', 'liron', 4, {})

    def test_invalid_age_upper_limit(self):
        with self.assertRaises(ValueError):
            stud = Student('208233650', 'liron', 121, {})

    def test_valid_id_9_digits(self):
        """check that id is exactly 9 digits"""
        self.assertEqual(len(self.student.i_d),9)

    def test_invalid_id_less_digits(self):
        """check that id is less than 9 digits"""
        with self.assertRaises(ValueError):
            stud = Student('20823365', 'liron', 25, {})

    def test_invalid_id_upper_digits(self):
        """check that id is less than 9 digits"""
        with self.assertRaises(ValueError):
            stud = Student('2082336554', 'liron', 25, {})

    def test_valid_name(self):
        self.assertEqual(self.student.name,'liron')

    def test_valid_id(self):
        self.assertEqual(self.student.i_d,'208233650')

    def test_valid_subject_grade_dic(self):
        self.assertEqual(self.student.subject_grade_dic,{'Math':90,'English':80})

    # End of initialize students args tests -------------------------------------------------------------------------

    # Start __eq__ function tests ---------------------------------------------------------------------------------------

    def test_valid_eq_student(self):
        stud = Student('208233650','liron',25,{'Math':90,'English':80})
        self.assertEqual(self.student,stud)

    def test_valid_eq_student_different_name(self):
        stud = Student('208233650','moshe',25,{'Math':90,'English':80})
        self.assertEqual(self.student,stud)

    def test_valid_eq_student_different_age(self):
        stud = Student('208233650','liron',45,{'Math':90,'English':80})
        self.assertEqual(self.student,stud)

    def test_valid_eq_student_different_dic(self):
        stud = Student('208233650','liron',45,{'Python':20})
        self.assertEqual(self.student,stud)

    def test_valid_eq_not_equal(self):
        """2 students with different id not equal"""
        stud = Student('304237654', 'liron', 45, {'Python': 20})
        self.assertFalse(self.student == stud)

    def test_eq_type(self):
        with self.assertRaises(TypeError):
            self.assertFalse(self.student == "123456789")


