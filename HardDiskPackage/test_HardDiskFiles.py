from unittest import TestCase
from HardDiskPackage.HardDiskFiles import HardDiskFiles
from HardDiskPackage.File import File
class TestHardDiskFiles(TestCase):

    def setUp(self):
        self.hd = HardDiskFiles(50)

    def test_used_space_full_hd(self):
        file1 = File("aaa", "txt",100)
        file2 = File("bbb", "txt",100)
        file3 = File("ccc", "txt",100)
        self.hd.files = [file1, file2, file3]
        self.assertEqual(300,self)


