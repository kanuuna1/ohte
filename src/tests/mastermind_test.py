import unittest
from mastermind import Mastermind


class TestMastermind(unittest.TestCase):
    def setUp(self):
        self.mastermind = Mastermind()

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.mastermind.size, 4)

    def test_code_length_is_correct(self):
        code = self.mastermind.create_code()
        self.assertEqual(len(code), 4)

    def test_compare_works_with_same_lists(self):
        list1=[0,1]
        list2 = list1
        self.assertEqual(self.mastermind.compare(list1, list2), ["black", "black"])
    

    def test_compare_works_with_black_and_white(self):
        list1=[0,1]
        list2 = [0,0]
        self.assertEqual(self.mastermind.compare(list1, list2), ["black", "white"])
    
    def test_compare_works_with_white(self):
        list1=[0,1]
        list2 = [1,0]
        self.assertEqual(self.mastermind.compare(list1, list2), ["white", "white"])
    
    def test_compare_works_with_no_whites(self):
        list1=[0,0]
        list2 = [1,1]
        self.assertEqual(self.mastermind.compare(list1, list2), [])