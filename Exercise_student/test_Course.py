from unittest import TestCase
from Exercise_student.Course import Course

class TestCourse(TestCase):

    def setUp(self):
        self.course1 = Course(45,"Math", 100)

    def test_init_valid(self):
        """test a simple valid case of init"""
        self.assertEqual(45, self.course1.course_num)
        self.assertEqual("Math", self.course1.course_name)
        self.assertEqual(100, self.course1.max_capacity)


    def test_init_valid_Negative_num(self):
        """test course number is not negative"""
        with self.assertRaises(TypeError):
            course1 = Course(-4, "Math", 100)

    def test_init_valid_course_name(self):
        with self.assertRaises(TypeError):
            course1 = Course(40, 543 , 100)

    def test_init_valid_max_capacity(self):
        with self.assertRaises(TypeError):
            course1 = Course(40, '543"' , -5)




