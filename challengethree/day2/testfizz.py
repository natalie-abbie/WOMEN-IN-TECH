from fizzbuzz import fizzbuzz
import unittest

class Testfizzbuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3,3), 'fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5,5), 'buzz')


    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(10,5), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()
