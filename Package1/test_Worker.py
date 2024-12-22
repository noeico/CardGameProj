from unittest import TestCase
from Package1.Worker import Worker
from unittest import mock
from unittest.mock import patch


class TestWorker(TestCase):
    def test_full_name(self):
        Sam = Worker("Sam", "Jackson", "2000", "may", "14", "dizingof", "il")
        self.assertEqual((Sam.full_name()), "Sam")


    def test_age(self):
        self.fail()

    def test_days_to_birthday(self):
        self.fail()

    def test_location_success(self):
        worker = Worker("Sam", "Jackson", 2000, 5, 14, "dizingof", "il")
        with patch ('Package1.Worker.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = "Success"
            print(worker.location())
            self.assertEqual("Success", worker.location())
