import unittest
from mastermind import Mastermind

class TestMastermind(unittest.TestCase):
    def setUp(self):
        self.mastermind = Mastermind(4)

    def test_code_length_is_correct(self):
        code = self.mastermind.create_code_without_duplicates()
        self.assertEqual(len(code), 4)
