from unittest import TestCase
from File import File


class TestFile(TestCase):
    def setUp(self):
        self.file = File('file1','docx',40)

    def tearDown(self):
        print('i am tear down')

    def test_init_valid(self):
       self.assertEqual('file1',self.file.name)
       self.assertEqual('docx',self.file.suffix)
       self.assertEqual('40',self.file.size)

    def test_init_invalid_negative_size(self):
        file1 = File('file1','docx',-100)
        self.assertEqual(0,file1.size)

    def test_init_invalid_size_type(self):
        with self.assertRaises(TypeError):
            file1 = File('file1', 'docx', 'test')

    def test_init_invalid_name_type(self):
        with self.assertRaises(TypeError):
            file1 = File('file1', 30, 30)

    def test_init_invalid_suffix_type(self):
        with self.assertRaises(TypeError):
            file1 = File(10, 'docx', 30)

    def test_eq_valid(self):
        eq_file=File('file1','docx',80)
        self.assertEqual(eq_file,self.file)
