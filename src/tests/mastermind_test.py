import unittest
from services.mastermind import Mastermind


class TestMastermind(unittest.TestCase):
    def setUp(self):
        self.mastermind = Mastermind()

    def test_size_is_correct(self):
        self.assertEqual(self.mastermind.size, 4)

    def test_code_length_is_correct(self):
        code = self.mastermind.create_code()
        self.assertEqual(len(code), 4)

    def test_compare_works_with_same_lists(self):
        list1=[0,1]
        list2 = list1
        self.assertEqual(self.mastermind.compare(list1, list2), ["black", "black"])
    

    def test_compare_works_with_black_and_white(self):
        list1=[1,1,2]
        list2 = [1,0,1]
        self.assertEqual(self.mastermind.compare(list1, list2), ["black", "white"])
    
    def test_compare_works_with_white(self):
        list1=[0,1]
        list2 = [1,0]
        self.assertEqual(self.mastermind.compare(list1, list2), ["white", "white"])
    
    def test_compare_works_with_no_whites(self):
        list1=[0,0]
        list2 = [1,1]
        self.assertEqual(self.mastermind.compare(list1, list2), [])

    def test_add_guess_doesnt_add_negatives(self):
        self.mastermind.add_guess(-1)
        self.assertEqual(self.mastermind.guess, [])
    
    def test_add_guess_doesnt_add_too_large_num(self):
        self.mastermind.add_guess(7)
        self.assertEqual(self.mastermind.guess, [])

    def test_add_guess_works(self):
        self.mastermind.add_guess(1)
        self.mastermind.add_guess(5)
        self.mastermind.add_guess(0)
        self.mastermind.add_guess(6)
        self.assertEqual(self.mastermind.guess, [1,5,0,6])
    
    def test_compare_guess_and_code_works(self):
        #self.code = [1]
        self.mastermind.code = [1]
        self.mastermind.add_guess(1)
        self.assertEqual(self.mastermind.compare(self.mastermind.guess, self.mastermind.code), ["black"])
    
    def test_add_turn_works(self):
        self.mastermind.add_turn()
        self.assertEqual(self.mastermind.turn, 1)
    
    def test_add_turn_works_when_too_large(self):
        for i in range (15):
            self.mastermind.add_turn()
        self.assertEqual(self.mastermind.turn, 10)