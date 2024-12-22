from unittest import TestCase
from Orly_solution.File import File


class TestFile(TestCase):
    def setUp(self):
        self.file = File("file1","docx",40)

    def test_init_valid(self):
        """Test a simple valid case of init"""
        self.assertEqual("file1",self.file.name)
        self.assertEqual("docx",self.file.suffix)
        self.assertEqual(40,self.file.size)

    def test_init_valid_short_suffix(self):
        """Test a valid case with 2 letters suffix"""
        file = File("file1", "ab", 50)
        self.assertEqual("file1", file.name)
        self.assertEqual("ab", file.suffix)
        self.assertEqual(50, file.size)

    def test_init_valid_long_suffix(self):
        """Test a valid case with 5 letters suffix"""
        file = File("file1", "abcde", 50)
        self.assertEqual("file1", file.name)
        self.assertEqual("abcde", file.suffix)
        self.assertEqual(50, file.size)

    def test_init_invalid_negative_size(self):
        """In case of a negative size, the size should be initialized to 0"""
        file = File("file1","txt",-100)
        self.assertEqual(0, file.size)

    def test_init_invalid_size_type(self):
        """In case of an invalid type of argument size. __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File("file1","txt","100")

    def test_init_invalid_name_type(self):
        """In case of an invalid type of argument name. __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File(12343,"txt",100)

    def test_init_invalid_suffix_type(self):
        """In case of an invalid type of argument suffix. __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File("file1",[1,2,3],100)

    def test_init_invalid_suffix_short(self):
        with self.assertRaises((ValueError)):
            file = File("file1","x",50)

    def test_init_invalid_suffix_long(self):
        with self.assertRaises((ValueError)):
            file = File("file1","abcdefg",50)

    def test_eq_valid(self):
        file = File("file1","docx",40)
        self.assertTrue(self.file == file)
        #self.assertEqual(file, self.file)

    def test_eq_valid_different_size(self):
        file = File("file1","docx",30)
        self.assertTrue(self.file == file)

    def test_eq_valid_suffix_not_equal(self):
        file = File("file1", "txt", 40)
        self.assertFalse(self.file == file)

    def test_eq_valid_name_not_equal(self):
        file = File("file2", "docx", 40)
        self.assertFalse(self.file == file)

    def test_eq_not_valid(self):
        self.assertFalse(self.file == 10)

    def test_gt_valid_True(self):
        file = File("file1", "docx", 30)
        self.assertTrue(self.file > file)

    def test_gt_valid_False(self):
        file = File("file1", "docx", 50)
        self.assertFalse(self.file > file)

    def test_gt_valid_False_equal(self):
        file = File("file1", "docx", 40)
        self.assertFalse(self.file > file)

    def test_gt_invalid(self):
        with self.assertRaises(TypeError):
            print(self.file > 10)