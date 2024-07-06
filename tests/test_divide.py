import unittest
from Check.divide import division
class Testdivide(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(division(2, 2), 1)
if __name__ == "__main__":
    unittest.main()