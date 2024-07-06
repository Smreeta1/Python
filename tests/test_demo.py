# import sys
# import os
import unittest

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
          
# current_dir = os.path.dirname(__file__)                               #returns the directory containing test_demo.py i.e. tests/
# parent_dir = os.path.abspath(os.path.join(current_dir, '..'))         #moves one level up from tests/ to Venv test/
# sys.path.insert(0, parent_dir)                                        #adds the parent directory to the start of the sys.path list, so that Python looks in Venv test/ first when trying to import modules.

# use: pip install .



from Check.demo import greet, add 
class TestMyFunctions(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(0, 0), 0.0)
        
       #Flase assertion 
        self.assertFalse(add(0, 0)== 0.1)
       #Type check
        self.assertIsInstance(add(1, 2), int)  #test fails as add() returns float only here in demo.py
        self.assertIsInstance(add(1, 2), float) #test ok
        self.assertIsInstance(add(1.5, 2.5), float)  # If add always returns float
        
if __name__ == '__main__':
    unittest.main()
