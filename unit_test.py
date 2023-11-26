import unittest
from text_edit_functions import sum_of_digits


class TestFunc(unittest.TestCase):
    def test_square(self):
        self.assertEqual(sum_of_digits('123'), 6)
        self.assertEqual(sum_of_digits('00000'), 0)
        self.assertEqual(sum_of_digits('21874681648'), 55)


if __name__ == '__main__':
    unittest.main()
