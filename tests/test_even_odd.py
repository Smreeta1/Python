import unittest
from Check.even_odd import check_even_odd

class TestEvenOdd(unittest.TestCase):

    def test_even_num(self):
        self.assertEqual(check_even_odd(0), "0 is even.")
        self.assertEqual(check_even_odd(2), "2 is even.")
        self.assertEqual(check_even_odd(10), "10 is even.")
     

    def test_odd_num(self):
        self.assertEqual(check_even_odd(1), "1 is odd.")
        self.assertEqual(check_even_odd(3), "3 is odd.")
    

if __name__ == "__main__":
    unittest.main()