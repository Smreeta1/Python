import unittest
from string_modify.reverse_str import reverse_string
class TestReverseString(unittest.TestCase):

    def test_reverse_str(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        
    def test_reverse_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")
        
if __name__ == '__main__':
    unittest.main()