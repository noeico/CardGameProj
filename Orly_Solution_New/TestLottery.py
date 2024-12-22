from unittest import TestCase, mock
from unittest.mock import patch
from tests.Lottery import Lottery

class TestLottery(TestCase):

    def setUp(self):
        self.lottery = Lottery()

    # using mock as a decorator
    @mock.patch('tests.Lottery.Lottery.rand_numbers', return_value=[10,31,11,20,45,20])
    def test_valid_numbers_False(self, mock_rand_numbers):
        # Tests a case in which a number is duplicated
        self.assertFalse(self.lottery.valid_numbers())
        print(self.lottery.numbers)

    @mock.patch('tests.Lottery.Lottery.rand_numbers', return_value=[10, 31, 11, 20, 67, 21])
    def test_valid_numbers_True(self, mock_rand_numbers):
        # Tests a case in which all numbers are unique
        self.assertTrue(self.lottery.valid_numbers())
        print(self.lottery.numbers)

    def test_valid_numbers_out_of_range(self):
        # using mock as a context manager
        with patch ('tests.Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value = [31, 0, 11, 12, 12, 20]
            print("out of range values", mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())
            mock_rand_num.return_value = [31, 11, 12, 12, 20, 46]
            print("out of range values", mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())
            mock_rand_num.return_value = [0, 31, 11, 12, 12, 20]
            print("out of range values", mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())


    def test_valid_numbers_in_range(self):
        # using mock as a context manager
        with patch('tests.Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value = [1, 31, 11, 12, 45, 20]
            print("in range values", mock_rand_num.return_value )
            self.assertTrue(self.lottery.valid_range())