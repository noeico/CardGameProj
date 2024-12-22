from unittest import TestCase, mock
from Orly_solution.Hard_Disk_Files import Hard_Disk_Files
from Orly_solution.File import File

class TestHard_Disk_Files(TestCase):
    def setUp(self):
        self.hd = Hard_Disk_Files(300)
        self.file1 = File("file1","py",50)
        self.file2 = File("file2","py",40)
        self.file3 = File("file3","docx",40)

    def test_used_space_empty(self):
        self.assertEqual(0, self.hd.used_space())

    def test_used_space_not_empty(self):
        self.hd.files=[self.file1,self.file2,self.file3]
        self.assertEqual(130,self.hd.used_space())

    def test_free_space_valid_not_empty(self):
        self.hd.files = [self.file1, self.file2, self.file3]
        self.assertEqual(170,self.hd.free_space())

    @mock.patch('Orly_solution.Hard_Disk_Files', return_value=300)
    def test_free_space_full_hd(self, mock_used_space):
        self.assertEqual(0, self.hd.free_space())

    def test_add_file_invalid_file(self):
        self.assertFalse(self.hd.add_file("abcdef"))
        self.assertEqual([],self.hd.files)

    def test_add_file_valid(self):
        self.assertTrue(self.hd.add_file(self.file1))
        self.assertEqual([self.file1],self.hd.files)
        self.assertIn(self.file1,self.hd.files)

    @mock.patch('Orly_solution.Hard_Disk_Files.Hard_Disk_Files.used_space', return_value=280)
    def test_free_space_empty_hd(self,mock_free_space):
        self.assertEqual(20, self.hd.free_space())


