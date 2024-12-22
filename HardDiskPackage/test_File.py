from unittest import TestCase
from HardDiskPackage.File import File


class TestFile(TestCase):
    def setUp(self):
        self.file = File("file1", "docx", 40)

    def tearDown(self):
        print("I am tear down")

    def test_init_valid(self):
        self.assertEqual("file1",self.file.name)
        self.assertEqual("docx", self.file.suffix)
        self.assertEqual(40, self.file.size)

    def test_init_invalid_negative_size(self):
        file = File("file1", "txt", -100)
        self.assertEqual(0, file.size)

    def test_init_invalid_size_type(self):
        """in case of an invalid type of arguments size, __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File("file1", "txt","100")

    def test_init_invalid_name_type(self):
        """in case of an invalid type of name, __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File(678, "txt", "100")

    def test_init_invalid_suffixame_type(self):
        """in case of an invalid type of suffix, __init__ should raise an exception"""
        with self.assertRaises(TypeError):
            file = File("file1", 543, "100")

    def test_init_invalid_suffix_short(self):
        with self.assertRaises(TypeError):
            file = File("file1", "a", 32)

    def test_init_invalid_suffix_short(self):
        with self.assertRaises(TypeError):
            file = File("file1", "aaaaaaa", 32)

    def test_eq_valid(self):
        file = File("file1", "docx", 40)
        self.assertTrue((self.file == file))

    def test_eq_valid_diffrent_size(self):
        file = File("file1", "docx", 30)
        self.assertTrue((self.file == file))

    def test_eq_valid_suffix_not_equal(self):
        file = File("file1", "txt", 40)
        self.assertTrue((self.file == file))

    def test_gt_valid_True(self):
        file = File("file1", "docx", 30)
        self.assertTrue((self.file > file))

    def test_gt_valid_True(self):
        file = File("file1", "docx", 50)
        self.assertFalse((self.file > file))

    def test_gt_invalid(self):
        with self.assertRaises(TypeError):
            print(self.file > 10)