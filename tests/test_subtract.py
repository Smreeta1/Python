import unittest
from Check.subtract import subtract
class TestSubtract(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
if __name__ == "__main__":
    unittest.main()