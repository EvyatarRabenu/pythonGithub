from unittest import TestCase,mock
from unittest.mock import patch
from studen_course_ex.Course import Course
from studen_course_ex.Student import Student



class TestCourse(TestCase):
    def setUp(self):
        self.course = Course('1234','python',5)
        student1 = Student('208233650', 'liron', 25, {'math': 90,'english':60})
        student2 = Student('303453350', 'tesler', 24, {'math': 70})
        student3 = Student('318233345', 'evyatar', 30, {'english': 70})
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)

    def test_valid_factor_added(self):
        self.course.add_factor('math',10)
        self.assertAlmostEqual(self.course.student_list[0].subject_grade_dic,{'math': 88,'english':60},places=2)
        self.assertAlmostEqual(self.course.student_list[1].subject_grade_dic,{'math': 77},places=2)
        self.assertAlmostEqual(self.course.student_list[2].subject_grade_dic,{'english': 70},places=2)

    @mock.patch('studen_course_ex.Course.Course.averages',return_value={'208233650':80,'384837374':80,'283273849':90})
    def test_many_weak_students(self,fck_mock):
        self.assertEqual(['208233650','384837374'],self.course.weak_students())

    @mock.patch('studen_course_ex.Course.Course.averages',return_value={})
    def test_empty_weak_students(self,fck_mock):
        self.assertEqual([],self.course.weak_students())



    # @mock.patch('Hard_DiskFile.HardDiskFiles.used_space', return_value=280)
    # def test_free_space_few_files(self, mock_used_space):
    #     """Test a case with a few files in the hd """
    #
    #     self.assertEqual(20, self.hd.free_space())

    # def test_free_space_empty_hd(self):
    #     with patch('Hard_DiskFile.HardDiskFiles.used_space') as mock_used_space:
    #         mock_used_space.return_value = 0
    #
    #         self.assertEqual(300, self.hd.free_space())

    # def add_factor(self, subject_name, factor):
    #     # Apply a factor to all students' grades for a specific subject.
    #     for student in self.student_list:
    #         student.calc_factor(subject_name, factor)