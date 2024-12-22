import numbers
from unittest import TestCase
from Package1.Lottery import Lottery
from unittest import mock
from unittest.mock import patch




class TestLottery(TestCase):

    def setUp(self):
        self.lottery = Lottery()
        self.numbers = self.lottery.rand_numbers()


    def test_rand_numbers(self):
        self.assertGreater()
        self.fail()

    def test_valid_numbers(self):
        for x in range(6):
            self.assertGreater(self.numbers[x],45, {self.numbers[x]}, "is bigger that 45")
        self.fail()

    def test_valid_range(self):
        self.fail()

    @mock.patch('Package1.Lottery.Lottery.rand_numbers' ,return_value =[10,20,30,40,12,34])
    def test_valid_numbers_False(self, mockInvalidNumbers):
        print(self.lottery.valid_numbers())
        print(self.lottery.rand_numbers())
        self.assertTrue(self.lottery.valid_numbers())


    def test_valid_range_True(self):
        with patch('Package1.Lottery.Lottery.rand_numbers') as mock_valid_range_T:
            mock_valid_range_T.return_value=[4,5,6,7,8,9]
            print(self.lottery.valid_range())
            print(self.lottery.rand_numbers())
            self.assertFalse((self.lottery.valid_range()))

