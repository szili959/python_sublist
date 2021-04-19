import unittest
from continental_task import identifySublist

class SubListTest(unittest.TestCase):

    def test_given(self):
        lst = [0, 'a', 'c', 4, 1, 2, 'b', 0, 2, 3]
        result = identifySublist(lst)
        self.assertEqual(result, (1, 6))

    def test_empty(self):
        lst = []
        result = identifySublist(lst)
        self.assertEqual(result, (0, 0))

    def test_char_only(self):
        lst = ['a', 'b', 'c']
        result = identifySublist(lst)
        self.assertEqual(result, (0, 0))

    def test_digit_only(self):
        lst = [1, 2, 3]
        result = identifySublist(lst)
        self.assertEqual(result, (0, 0))

    def test_one_char_only(self):
        lst = [1, 2, 'a', 3]
        result = identifySublist(lst)
        self.assertEqual(result, (1, 2))
    
    def test_one_element_only(self):
        lst = ['a']
        result = identifySublist(lst)
        self.assertEqual(result, (0, 0))

    def test_one_and_one(self):
        lst = ['a', 1]
        result = identifySublist(lst)
        self.assertEqual(result, (0, 1))

if __name__ == '__main__':
    unittest.main()