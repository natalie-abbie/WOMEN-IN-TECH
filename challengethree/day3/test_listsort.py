import unittest

from list_sort import list_sort


class listsortTest(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(list_sort(7), 'Invalid Input')

    def test_string_input(self):
        self.assertEqual(list_sort('string'), 'Invalid Input')

    def test_empty_list(self):
        self.assertEqual(list_sort([]), {'evens': [], 'odds': [], 'chars': []})

    def test_no_string(self):
        self.assertEqual(
            list_sort([1,2,3,4,5,]),
            {'evens': [2, 4], 'odds': [1, 3, 5], 'chars': []}
            )

    def test_no_even(self):
        self.assertEqual(
            list_sort([1,3,5, 'a', 'b']),
            {'evens': [], 'odds': [1, 3, 5,], 'chars': ['a', 'b']}
            )

    def test_no_odd(self):
        self.assertEqual(
            list_sort([2,4, 'a', 'b']),
            {'evens': [2, 4], 'odds': [], 'chars': ['a', 'b']}
            )

    def test_complete_list(self):
        self.assertEqual(
            list_sort([1,2,3,4,5, 'a', 'b']),
            {'evens': [2, 4], 'odds': [1, 3, 5,], 'chars': ['a', 'b']}
            )

if __name__ == '__main__':
    unittest.main()
